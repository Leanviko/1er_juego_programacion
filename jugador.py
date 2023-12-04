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

def movimiento_jugador(jugador_parametros,mover_derecha,mover_izquierda, VEL_JUGADOR, ANCHO_VENTANA):
    jugador_parametros["jugador_imagen_scalada"] = pygame.transform.scale_by(jugador_parametros["jugador_imagen"],0.2)
    jugador_parametros["jugador_rect"] = jugador_parametros["jugador_imagen_scalada"].get_rect()
    jugador_parametros["jugador_rect"].centerx = jugador_parametros["centro_x"]
    jugador_parametros["jugador_rect"].centery = jugador_parametros["centro_y"]
    
    #limites jugador
    if mover_derecha == True and jugador_parametros["jugador_rect"].right <= ANCHO_VENTANA:
        jugador_parametros["centro_x"] += VEL_JUGADOR
    if mover_izquierda == True and jugador_parametros["jugador_rect"].left >= 0:
        jugador_parametros["centro_x"] -= VEL_JUGADOR

    

def cambiar_tamaño_jugador(jugador_parametros):

    """
    cambia el tamaño del jugador y la imagen segun el color

    Args:
    -sel_col_jug (int): Color del jugador
    -ancho_jugador (int):largo del jugador
    
    """
    sel_col_jug = jugador_parametros["sel_col_jug"]
    ancho_jugador = jugador_parametros["ancho_jugador"]
    #jugador_imagen = jugador_parametros["jugador_imagen"]

    if sel_col_jug == 0:
        
        #color_actual = 0
        if ancho_jugador == 1:
            jugador_parametros["jugador_imagen"] = pygame.image.load(J_VERDE_LARGO).convert_alpha()
        else:
            jugador_parametros["jugador_imagen"] = pygame.image.load(J_VERDE_CORTO).convert_alpha()
    elif sel_col_jug == 1:
        
        #color_actual = 1
        if ancho_jugador == 1:
            jugador_parametros["jugador_imagen"] = pygame.image.load(J_AZUL_LARGO).convert_alpha()
        else:
            jugador_parametros["jugador_imagen"] = pygame.image.load(J_AZUL_CORTO).convert_alpha()
    elif sel_col_jug == 2:
        
        #color_actual = 2
        if ancho_jugador == 1:
            jugador_parametros["jugador_imagen"] = pygame.image.load(J_ROJO_LARGO).convert_alpha()
        else:
            jugador_parametros["jugador_imagen"] = pygame.image.load(J_ROJO_CORTO).convert_alpha()

    
    
    #return jugador_imagen, color_actual