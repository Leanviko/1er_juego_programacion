import pygame
import json

with open("configuracion.json","r") as conf:
    configuracion = json.load(conf)

J_ROJO_LARGO = configuracion["jugador_rojo_largo"]
J_ROJO_CORTO = configuracion["jugador_rojo_corto"]
J_AZUL_LARGO = configuracion["jugador_azul_largo"]
J_AZUL_CORTO = configuracion["jugador_azul_corto"]
J_VERDE_LARGO = configuracion["jugador_verde_largo"]
J_VERDE_CORTO = configuracion["jugador_verde_corto"]

def cambiar_tamaño_jugador(sel_col_jug,ancho_jugador,jugador_rect):

    if sel_col_jug == 0:
        #pygame.draw.rect(pantalla,VERDE,jugador_rect)
        color_actual = 0
        if ancho_jugador == 1:
            jugador_imagen = pygame.image.load(J_VERDE_LARGO).convert_alpha()
        else:
            jugador_imagen = pygame.image.load(J_VERDE_CORTO).convert_alpha()
    elif sel_col_jug == 1:
        #pygame.draw.rect(pantalla,AZUL,jugador_rect)
        color_actual = 1
        if ancho_jugador == 1:
            jugador_imagen = pygame.image.load(J_AZUL_LARGO).convert_alpha()
        else:
            jugador_imagen = pygame.image.load(J_AZUL_CORTO).convert_alpha()
    elif sel_col_jug == 2:
        #pygame.draw.rect(pantalla,ROJO,jugador_rect)
        color_actual = 2
        if ancho_jugador == 1:
            jugador_imagen = pygame.image.load(J_ROJO_LARGO).convert_alpha()
        else:
            jugador_imagen = pygame.image.load(J_ROJO_CORTO).convert_alpha()

    
    
    return jugador_imagen, color_actual