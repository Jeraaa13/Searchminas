from juego import Juego
from tablero import Tablero

tamaño_tablero = (10,10)
prob = 0.1
tablero = Tablero(tamaño_tablero, prob)

tamaño_pantalla = (500,500)
juego = Juego(tablero, tamaño_pantalla, tamaño_tablero, prob)

juego.run()