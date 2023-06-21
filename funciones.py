import pygame, sys, pygame_gui
from boton import Boton
from database import *
import colores

def mostrar_pantalla_ganar(pantalla, tiempo_final):
    WIDTH, HEIGHT = 500, 500
    pygame.display.set_caption("Ganaste")
    RELOJ = pygame.time.Clock()
    MANAGER = pygame_gui.UIManager((WIDTH, HEIGHT))
    flecha_atras = pygame.image.load("imagenes/0arrow.png")
    entrada_de_texto = pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect((50,200),(400,50)), manager=MANAGER,
                                        object_id="#main_text_entry")
    entrada_de_texto.set_text_length_limit(10)
    tiempo = pygame.image.load("imagenes/tiempopiola.png")
    tiempo_rect = tiempo.get_rect()
    tiempo_rect.x, tiempo_rect.y = 0,0

    while True:
        pantalla.blit(tiempo, tiempo_rect)
        pantalla.blit(flecha_atras, (0,0))

        menu_mouse_pos = pygame.mouse.get_pos()

        boton_atras = Boton(imagen=pygame.image.load("imagenes/0arrowholdea.png"), pos=(0,0), tamaño=(50,50))

        UI_REFRESH_RATE = RELOJ.tick(60)/1000
        string = f"{tiempo_final}"
        font = pygame.font.SysFont("MINE-SWEEPER Regular", 32)
        tiempo_numero = font.render(string, True, (4,132,4))
        pantalla.blit(tiempo_numero, (175,100))

        boton_atras.si_holdea(pantalla, menu_mouse_pos)

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if evento.type == pygame_gui.UI_TEXT_ENTRY_FINISHED and evento.ui_object_id == "#main_text_entry":
                crear_tabla_jugadores()
                modificar_tabla_jugadores(evento.text, str(tiempo_final))
            if evento.type == pygame.MOUSEBUTTONDOWN:
                if boton_atras.si_clickea(menu_mouse_pos):
                    return True
            MANAGER.process_events(evento)

        MANAGER.update(UI_REFRESH_RATE)
        MANAGER.draw_ui(pantalla)
        pygame.display.update()
        pygame.display.flip()

def mostrar_pantalla_perder(pantalla):
    gameover = pygame.image.load("imagenes/gameover.png")
    flecha_atras = pygame.image.load("imagenes/0arrow.png")
    reiniciar = pygame.image.load("imagenes/0reset.png")
    pygame.display.set_caption("Perdiste")

    while True:
        pantalla.blit(gameover, (50,100))
        pantalla.blit(flecha_atras, (100,400))
        pantalla.blit(reiniciar, (350,400))

        menu_mouse_pos = pygame.mouse.get_pos()

        boton_atras = Boton(imagen=pygame.image.load("imagenes/0arrowholdea.png"), pos=(100,400), tamaño=(50,50))
        boton_reiniciar = Boton(imagen=pygame.image.load("imagenes/0resetholdea.png"), pos=(350,400), tamaño=(50,50))

        for boton in [boton_atras, boton_reiniciar]:
            boton.si_holdea(pantalla, menu_mouse_pos)

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if evento.type == pygame.MOUSEBUTTONDOWN:
                if boton_atras.si_clickea(menu_mouse_pos):
                    return "volver_al_menu"
                if boton_reiniciar.si_clickea(menu_mouse_pos):
                    return "volver_a_jugar"

        pygame.display.flip()

def mostrar_tops(pantalla):
    pygame.display.set_caption("Tops")
    menu_tops = pygame.image.load("imagenes/topmenu.png")
    flecha_atras = pygame.image.load("imagenes/0arrow.png")
    font = pygame.font.SysFont("MINE-SWEEPER Regular", 20)

    while True:
        pantalla.blit(menu_tops, (0,0))
        pantalla.blit(flecha_atras, (0,0))

        menu_mouse_pos = pygame.mouse.get_pos()

        boton_atras = Boton(imagen=pygame.image.load("imagenes/0arrowholdea.png"), pos=(0,0), tamaño=(50,50))

        boton_atras.si_holdea(pantalla, menu_mouse_pos)

        try: 
            resultados = leer_tabla_jugadores()

            y = 51
            posicion_juego = 1

            for nombre, puntacion in resultados:
                texto = font.render(f"{posicion_juego}. {nombre} - {puntacion}", True, colores.BLUE)
                pantalla.blit(texto, (55, y))
                y += 41
                posicion_juego += 1
        except sqlite3.OperationalError:
            pass

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if evento.type == pygame.MOUSEBUTTONDOWN:
                if boton_atras.si_clickea(menu_mouse_pos):
                    return "volver_al_menu"
                
        pygame.display.flip()

def menu(pantalla):
    pygame.display.set_caption("Searchminas")
    ancho_ventana = pantalla.get_size()[0]
    alto_ventana = pantalla.get_size()[1]
    background = pygame.image.load("imagenes/fondo.png")
    background = pygame.transform.scale(background, (ancho_ventana, alto_ventana))
    while True:
        pantalla.blit(background,(0,0))

        menu_mouse_pos = pygame.mouse.get_pos()

        play_boton = Boton(imagen=pygame.image.load("imagenes/botonplaypresionado.png"), pos=(150,200), tamaño=(200,50))

        top_boton = Boton(imagen=pygame.image.load("imagenes/top.png"), pos=(175,300), tamaño=(150,50))

        exit_boton = Boton(imagen=pygame.image.load("imagenes/exit.png"), pos=(150,400), tamaño=(200,50))

        for boton in [play_boton, top_boton, exit_boton]:
            boton.si_holdea(pantalla,menu_mouse_pos)

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if evento.type == pygame.MOUSEBUTTONDOWN:
                if play_boton.si_clickea(menu_mouse_pos):
                    return "jugar"
                if top_boton.si_clickea(menu_mouse_pos):
                    return "tops"
                if exit_boton.si_clickea(menu_mouse_pos):
                    return "salir"

        pygame.display.flip()