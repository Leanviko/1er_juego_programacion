import pygame
import json

"""
lista de los bloque y sus atributos

"""

with open("configuracion.json","r") as conf:
    configuracion = json.load(conf)

ANCHO_BLOQUE = configuracion["ancho_bloque"]
ALTO_BLOQUE = configuracion["alto_bloque"]
ESPACIADO = configuracion["espaciado"]

#posicion primer bloque
x = 140
y = 170
rec_x = (ANCHO_BLOQUE+ESPACIADO)
rec_y = (ALTO_BLOQUE+ESPACIADO)

esq_bloques = [
    #primer fila
    {"rect": pygame.Rect(x, y, ANCHO_BLOQUE, ALTO_BLOQUE), "golpes": 1},
    {"rect": pygame.Rect(x+rec_x*1, y, ANCHO_BLOQUE, ALTO_BLOQUE), "golpes": 1},
    {"rect": pygame.Rect(x+rec_x*2, y, ANCHO_BLOQUE, ALTO_BLOQUE), "golpes": 1},
    {"rect": pygame.Rect(x+rec_x*3, y, ANCHO_BLOQUE, ALTO_BLOQUE), "golpes": 1},
    {"rect": pygame.Rect(x+rec_x*4, y, ANCHO_BLOQUE, ALTO_BLOQUE), "golpes": 1},
    {"rect": pygame.Rect(x+rec_x*5, y, ANCHO_BLOQUE, ALTO_BLOQUE), "golpes": 1},
    {"rect": pygame.Rect(x+rec_x*6, y, ANCHO_BLOQUE, ALTO_BLOQUE), "golpes": 1},
    {"rect": pygame.Rect(x+rec_x*7, y, ANCHO_BLOQUE, ALTO_BLOQUE), "golpes": 1},
    {"rect": pygame.Rect(x+rec_x*8, y, ANCHO_BLOQUE, ALTO_BLOQUE), "golpes": 1},
    #{"rect": pygame.Rect(x+rec_x*9, y, ANCHO_BLOQUE, ALTO_BLOQUE), "golpes": 1},

    # #segunda fila
    # {"rect": pygame.Rect(x, y+rec_y, ANCHO_BLOQUE, ALTO_BLOQUE), "golpes": 2},
    # {"rect": pygame.Rect(x+rec_x*1, y+rec_y, ANCHO_BLOQUE, ALTO_BLOQUE), "golpes": 2},
    # {"rect": pygame.Rect(x+rec_x*2, y+rec_y, ANCHO_BLOQUE, ALTO_BLOQUE), "golpes": 2},
    # {"rect": pygame.Rect(x+rec_x*3, y+rec_y, ANCHO_BLOQUE, ALTO_BLOQUE), "golpes": 2},
    # {"rect": pygame.Rect(x+rec_x*4, y+rec_y, ANCHO_BLOQUE, ALTO_BLOQUE), "golpes": 2},
    # {"rect": pygame.Rect(x+rec_x*5, y+rec_y, ANCHO_BLOQUE, ALTO_BLOQUE), "golpes": 2},
    # {"rect": pygame.Rect(x+rec_x*6, y+rec_y, ANCHO_BLOQUE, ALTO_BLOQUE), "golpes": 2},
    # {"rect": pygame.Rect(x+rec_x*7, y+rec_y, ANCHO_BLOQUE, ALTO_BLOQUE), "golpes": 2},
    # {"rect": pygame.Rect(x+rec_x*8, y+rec_y, ANCHO_BLOQUE, ALTO_BLOQUE), "golpes": 2},
    # #{"rect": pygame.Rect(x+rec_x*9, y+rec_y, ANCHO_BLOQUE, ALTO_BLOQUE), "golpes": 2},


    # #tercer fila
    # {"rect": pygame.Rect(x, y+rec_y*2, ANCHO_BLOQUE, ALTO_BLOQUE), "golpes": 3},
    # {"rect": pygame.Rect(x+rec_x*1, y+rec_y*2, ANCHO_BLOQUE, ALTO_BLOQUE), "golpes": 3},
    # {"rect": pygame.Rect(x+rec_x*2, y+rec_y*2, ANCHO_BLOQUE, ALTO_BLOQUE), "golpes": 3},
    # {"rect": pygame.Rect(x+rec_x*3, y+rec_y*2, ANCHO_BLOQUE, ALTO_BLOQUE), "golpes": 3},
    # {"rect": pygame.Rect(x+rec_x*4, y+rec_y*2, ANCHO_BLOQUE, ALTO_BLOQUE), "golpes": 3},
    # {"rect": pygame.Rect(x+rec_x*5, y+rec_y*2, ANCHO_BLOQUE, ALTO_BLOQUE), "golpes": 3},
    # {"rect": pygame.Rect(x+rec_x*6, y+rec_y*2, ANCHO_BLOQUE, ALTO_BLOQUE), "golpes": 3},
    # {"rect": pygame.Rect(x+rec_x*7, y+rec_y*2, ANCHO_BLOQUE, ALTO_BLOQUE), "golpes": 3},
    # {"rect": pygame.Rect(x+rec_x*8, y+rec_y*2, ANCHO_BLOQUE, ALTO_BLOQUE), "golpes": 3},
    # #{"rect": pygame.Rect(x+rec_x*9, y+rec_y*2, ANCHO_BLOQUE, ALTO_BLOQUE), "golpes": 3},

    # #cuarta fila
    # {"rect": pygame.Rect(x, y+rec_y*3, ANCHO_BLOQUE, ALTO_BLOQUE), "golpes": 1},
    # {"rect": pygame.Rect(x+rec_x*1, y+rec_y*3, ANCHO_BLOQUE, ALTO_BLOQUE), "golpes": 1},
    # {"rect": pygame.Rect(x+rec_x*2, y+rec_y*3, ANCHO_BLOQUE, ALTO_BLOQUE), "golpes": 1},
    # {"rect": pygame.Rect(x+rec_x*3, y+rec_y*3, ANCHO_BLOQUE, ALTO_BLOQUE), "golpes": 1},
    # {"rect": pygame.Rect(x+rec_x*4, y+rec_y*3, ANCHO_BLOQUE, ALTO_BLOQUE), "golpes": 1},
    # {"rect": pygame.Rect(x+rec_x*5, y+rec_y*3, ANCHO_BLOQUE, ALTO_BLOQUE), "golpes": 1},
    # {"rect": pygame.Rect(x+rec_x*6, y+rec_y*3, ANCHO_BLOQUE, ALTO_BLOQUE), "golpes": 1},
    # {"rect": pygame.Rect(x+rec_x*7, y+rec_y*3, ANCHO_BLOQUE, ALTO_BLOQUE), "golpes": 1},
    # {"rect": pygame.Rect(x+rec_x*8, y+rec_y*3, ANCHO_BLOQUE, ALTO_BLOQUE), "golpes": 1},
    # #{"rect": pygame.Rect(x+rec_x*9, y+rec_y*3, ANCHO_BLOQUE, ALTO_BLOQUE), "golpes":1},
]