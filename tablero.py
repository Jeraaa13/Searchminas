from bloque import Bloque
from random import random

class Tablero:
    def __init__(self, tamaño, prob):
        self.tamaño = tamaño
        self.prob = prob
        self.perdio = False
        self.gano = False
        self.numeros_clickeado = 0
        self.cont_no_bombas = 0
        self.crearTablero()

    def crearTablero(self):
        self.matriz = []
        for fila in range(self.tamaño[0]):
            fila = []
            for col in range(self.tamaño[1]):
                tiene_bomba = random() < self.prob
                if not tiene_bomba:
                    self.cont_no_bombas += 1
                bloque = Bloque(tiene_bomba)
                fila.append(bloque)
            self.matriz.append(fila)
        self.crear_vecinos()

    def crear_vecinos(self):
        for fila in range(self.tamaño[0]):
            for col in range(self.tamaño[1]):
                indice = (fila,col)
                bloque = self.matriz[indice[0]][indice[1]]
                vecinos = self.get_lista_vecinos(indice)
                bloque.crear_vecinos(vecinos)

    def get_lista_vecinos(self, indice):
        vecinos = []
        for fila in range(indice[0] - 1, indice[0] + 2):
            for col in range(indice[1] - 1, indice[1] + 2):
                fuera_limites = fila < 0 or fila >= self.tamaño[0] or col < 0 or col >= self.tamaño[1]
                igual = fila == indice[0] and col == indice[1]
                if igual or fuera_limites:
                    continue
                vecinos.append(self.get_bloque((fila,col)))
        return vecinos

    def get_tamaño(self):
        return self.tamaño
    
    def get_bloque(self, indice):
        try:
            return self.matriz[indice[0]][indice[1]]
        except IndexError:
            print("Fuera de rango")
    
    def manejar_click(self, bloque, bandera):
        if bloque.get_fue_clickeado() or (not bandera and bloque.get_tiene_bandera()):
            return
        if bandera:
            bloque.alternar_bandera()
            return
        bloque.click()
        if bloque.get_tiene_bomba():
            self.perdio = True
            return
        self.numeros_clickeado += 1
        if bloque.get_numero_cerca() != 0:
            return
        for vecino in bloque.get_vecinos():
            if not vecino.get_tiene_bomba() and not vecino.get_fue_clickeado():
                self.manejar_click(vecino, False)
        
    def get_perdio(self):
        return self.perdio

    def get_gano(self):
        return self.cont_no_bombas == self.numeros_clickeado