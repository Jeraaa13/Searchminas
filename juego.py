import pygame
import os
import time
from tablero import Tablero
from database import *
import sys
from funciones import *

class Juego():
    def __init__(self, tablero, tamaño_pantalla, tamaño_tablero, prob):
        self.tamaño_tablero = tamaño_tablero
        self.prob = prob
        self.tablero = tablero
        self.tamaño_pantalla = tamaño_pantalla
        self.tiempo_inicial = 0.0
        self.tamaño_bloque = self.tamaño_pantalla[0] // self.tablero.get_tamaño()[0], self.tamaño_pantalla[1] // self.tablero.get_tamaño()[1]
        self.cargar_imagenes()

    def run(self):
        pygame.init()
        self.pantalla = pygame.display.set_mode(self.tamaño_pantalla)
        #Creo el menu
        eleccion = menu(self.pantalla)
        if eleccion == "jugar":
            self.iniciar_juego()
        elif eleccion == "tops":
            #Si elige ver los tops llamo a la funcion
            volver = mostrar_tops(self.pantalla)
            if volver:
                self.volver_al_menu()
        elif eleccion == "salir":
            pygame.quit()
            sys.exit()

    def iniciar_juego(self):
        pygame.display.set_caption("Jugando Searchminas")
        self.tiempo_inicial = round(time.time(), 2)
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    click_derecho = pygame.mouse.get_pressed()[2]
                    self.manejar_click(pos, click_derecho)
            self.dibujar()
            if self.tablero.get_perdio():
                self.al_perder()
            if self.tablero.get_gano():
                self.al_ganar()
            pygame.display.flip()

    def dibujar(self):
        coordenadas = (0,0)
        for fila in range(self.tablero.get_tamaño()[0]):
            for col in range(self.tablero.get_tamaño()[1]):
                indice = (fila,col)
                bloque = self.tablero.get_bloque(indice)
                imagen = self.get_imagen(bloque)
                self.pantalla.blit(imagen, coordenadas)
                coordenadas = coordenadas[0] + self.tamaño_bloque[0], coordenadas[1]
            coordenadas = 0, coordenadas[1] + self.tamaño_bloque[1]

    def cargar_imagenes(self):
        self.imagenes = {}
        for nombre_imagen in os.listdir("imagenes"):
            imagen = pygame.image.load(r"imagenes/" + nombre_imagen)
            imagen = pygame.transform.scale(imagen, self.tamaño_bloque)
            self.imagenes[nombre_imagen.split(".")[0]] = imagen

    def get_imagen(self, bloque):
        string = None
        if bloque.get_fue_clickeado():
            string = "bomb-at-clicked-block" if bloque.get_tiene_bomba() else str(bloque.get_numero_cerca())
        else:
            string = "flag" if bloque.get_tiene_bandera() else "empty-block"
        return self.imagenes[string]
    
    def manejar_click(self, pos, click_derecho):
        if self.tablero.get_perdio():
            return
        indice = pos[1] // self.tamaño_bloque[1], pos[0] // self.tamaño_bloque[0]
        bloque = self.tablero.get_bloque(indice)
        self.tablero.manejar_click(bloque, click_derecho)

    def al_perder(self):
        sound = pygame.mixer.Sound("sonidos/tnt.mp3")
        sound.play()
        eleccion = mostrar_pantalla_perder(self.pantalla)
        if eleccion == "volver_a_jugar":
            self.reiniciar_juego()
        elif eleccion == "volver_al_menu":
            self.volver_al_menu()
            
    def reiniciar_juego(self):
        pygame.display.set_caption("Jugando Searchminas")
        self.tablero = Tablero(self.tamaño_tablero, self.prob)
        self.tiempo_inicial = round(time.time(), 2)

    def volver_al_menu(self):
        self.tablero = Tablero(self.tamaño_tablero, self.prob)
        self.run()

    def al_ganar(self):
        self.tiempo_final = round(time.time() - self.tiempo_inicial, 2)
        sound = pygame.mixer.Sound("sonidos/win.wav")
        sound.play()
        eleccion_volver_al_menu = mostrar_pantalla_ganar(self.pantalla, self.tiempo_final)
        if eleccion_volver_al_menu:
            self.volver_al_menu()

