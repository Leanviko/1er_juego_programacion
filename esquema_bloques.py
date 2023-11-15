import pygame
import json

with open("configuracion.json","r") as conf:
    configuracion = json.load(conf)

ANCHO_BLOQUE = configuracion["ancho_bloque"]
ALTO_BLOQUE = configuracion["alto_bloque"]

esq_bloques = [
    #primer fila
    {"rect": pygame.Rect(100, 100, ANCHO_BLOQUE, ALTO_BLOQUE), "tipo": "facil", "golpes": 1},
    {"rect": pygame.Rect(160, 100, ANCHO_BLOQUE, ALTO_BLOQUE), "tipo": "dificil", "golpes": 3},
    {"rect": pygame.Rect(220, 100, ANCHO_BLOQUE, ALTO_BLOQUE), "tipo": "facil", "golpes": 1},
    {"rect": pygame.Rect(280, 100, ANCHO_BLOQUE, ALTO_BLOQUE), "tipo": "dificil", "golpes": 3},
    {"rect": pygame.Rect(340, 100, ANCHO_BLOQUE, ALTO_BLOQUE), "tipo": "medio", "golpes": 2},
    {"rect": pygame.Rect(400, 100, ANCHO_BLOQUE, ALTO_BLOQUE), "tipo": "dificil", "golpes": 3},
    {"rect": pygame.Rect(460, 100, ANCHO_BLOQUE, ALTO_BLOQUE), "tipo": "dificil", "golpes": 3},
    {"rect": pygame.Rect(520, 100, ANCHO_BLOQUE, ALTO_BLOQUE), "tipo": "medio", "golpes": 2},
    {"rect": pygame.Rect(580, 100, ANCHO_BLOQUE, ALTO_BLOQUE), "tipo": "dificil", "golpes": 3},
    {"rect": pygame.Rect(640, 100, ANCHO_BLOQUE, ALTO_BLOQUE), "tipo": "medio", "golpes": 2},

    #segunda fila
    {"rect": pygame.Rect(100, 130, ANCHO_BLOQUE, ALTO_BLOQUE), "tipo": "facil", "golpes": 1},
    {"rect": pygame.Rect(160, 130, ANCHO_BLOQUE, ALTO_BLOQUE), "tipo": "dificil", "golpes": 3},
    {"rect": pygame.Rect(220, 130, ANCHO_BLOQUE, ALTO_BLOQUE), "tipo": "facil", "golpes": 1},
    {"rect": pygame.Rect(280, 130, ANCHO_BLOQUE, ALTO_BLOQUE), "tipo": "dificil", "golpes": 3},
    {"rect": pygame.Rect(340, 130, ANCHO_BLOQUE, ALTO_BLOQUE), "tipo": "facil", "golpes": 1},
    {"rect": pygame.Rect(400, 130, ANCHO_BLOQUE, ALTO_BLOQUE), "tipo": "dificil", "golpes": 3},
    {"rect": pygame.Rect(460, 130, ANCHO_BLOQUE, ALTO_BLOQUE), "tipo": "dificil", "golpes": 3},
    {"rect": pygame.Rect(520, 130, ANCHO_BLOQUE, ALTO_BLOQUE), "tipo": "facil", "golpes": 1},
    {"rect": pygame.Rect(580, 130, ANCHO_BLOQUE, ALTO_BLOQUE), "tipo": "dificil", "golpes": 3},
    {"rect": pygame.Rect(640, 130, ANCHO_BLOQUE, ALTO_BLOQUE), "tipo": "dificil", "golpes": 3},

    #tercer fila
    {"rect": pygame.Rect(100, 160, ANCHO_BLOQUE, ALTO_BLOQUE), "tipo": "facil", "golpes": 1},
    {"rect": pygame.Rect(160, 160, ANCHO_BLOQUE, ALTO_BLOQUE), "tipo": "dificil", "golpes": 3},
    {"rect": pygame.Rect(220, 160, ANCHO_BLOQUE, ALTO_BLOQUE), "tipo": "facil", "golpes": 1},
    {"rect": pygame.Rect(280, 160, ANCHO_BLOQUE, ALTO_BLOQUE), "tipo": "dificil", "golpes": 3},
    {"rect": pygame.Rect(340, 160, ANCHO_BLOQUE, ALTO_BLOQUE), "tipo": "facil", "golpes": 1},
    {"rect": pygame.Rect(400, 160, ANCHO_BLOQUE, ALTO_BLOQUE), "tipo": "dificil", "golpes": 3},
    {"rect": pygame.Rect(460, 160, ANCHO_BLOQUE, ALTO_BLOQUE), "tipo": "dificil", "golpes": 3},
    {"rect": pygame.Rect(520, 160, ANCHO_BLOQUE, ALTO_BLOQUE), "tipo": "facil", "golpes": 1},
    {"rect": pygame.Rect(580, 160, ANCHO_BLOQUE, ALTO_BLOQUE), "tipo": "dificil", "golpes": 3},
    {"rect": pygame.Rect(640, 160, ANCHO_BLOQUE, ALTO_BLOQUE), "tipo": "dificil", "golpes": 3},

    #cuarta fila
    {"rect": pygame.Rect(100, 190, ANCHO_BLOQUE, ALTO_BLOQUE), "tipo": "facil", "golpes": 1},
    {"rect": pygame.Rect(160, 190, ANCHO_BLOQUE, ALTO_BLOQUE), "tipo": "dificil", "golpes": 3},
    {"rect": pygame.Rect(220, 190, ANCHO_BLOQUE, ALTO_BLOQUE), "tipo": "facil", "golpes": 1},
    {"rect": pygame.Rect(280, 190, ANCHO_BLOQUE, ALTO_BLOQUE), "tipo": "dificil", "golpes": 3},
    {"rect": pygame.Rect(340, 190, ANCHO_BLOQUE, ALTO_BLOQUE), "tipo": "facil", "golpes": 1},
    {"rect": pygame.Rect(400, 190, ANCHO_BLOQUE, ALTO_BLOQUE), "tipo": "dificil", "golpes": 3},
    {"rect": pygame.Rect(460, 190, ANCHO_BLOQUE, ALTO_BLOQUE), "tipo": "dificil", "golpes": 1},
    {"rect": pygame.Rect(520, 190, ANCHO_BLOQUE, ALTO_BLOQUE), "tipo": "facil", "golpes": 3},
    {"rect": pygame.Rect(580, 190, ANCHO_BLOQUE, ALTO_BLOQUE), "tipo": "dificil", "golpes": 1},
    {"rect": pygame.Rect(640, 190, ANCHO_BLOQUE, ALTO_BLOQUE), "tipo": "dificil", "golpes": 3},

]