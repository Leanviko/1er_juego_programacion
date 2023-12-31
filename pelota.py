import pygame
from assets import *

def pelota_logica(pelota_parametros, jugador_parametros, ANCHO_VENTANA, ALTO_VENTANA, datos_pantalla ,rebote):

    """
    Logica de movimiento y atributos de la pelota

    Args:
    -pelota_rect : rectangulo de la pelota
    -jugador_rect : rectangulo del jugador
    -vel_x (int): posicion de la pelota en el eje x
    -vel_y (int): posicion de la pelota en el eje y
    -ancho_ventana (int): ancho de la ventana de juego
    -alto_ventana (int): alto de la ventana de juego
    -vidas (int): vidas del jugador
    -sel_col_jug (int): color del la plataforma del jugador
    -sel_col_pelota (int): color de la pelota 
    -sonido (.wav): sonido de la pelota al impactar
    
    """

    
    pelota_parametros["pelota_rect"].centerx += pelota_parametros["vel_x"] 
    pelota_parametros["pelota_rect"].centery += pelota_parametros["vel_y"] 

    if pelota_parametros["pelota_rect"].right >= ANCHO_VENTANA:
        pelota_parametros["pelota_rect"].right = ANCHO_VENTANA
        pelota_parametros["vel_x"] *= -1
        rebote.play()
    if  pelota_parametros["pelota_rect"].left <= 0:
        pelota_parametros["pelota_rect"].left = 0
        pelota_parametros["vel_x"] *= -1
        rebote.play()
    if pelota_parametros["pelota_rect"].top <= 0:
        pelota_parametros["pelota_rect"].top = 0
        pelota_parametros["vel_y"] *= -1
        rebote.play()
    if pelota_parametros["pelota_rect"].top > ALTO_VENTANA:
        pelota_parametros["pelota_rect"].midbottom = jugador_parametros["jugador_rect"].midtop
        
        datos_pantalla["vidas"] -= 1
        pelota_parametros["vel_y"] *= -1 
    
    if pygame.Rect.colliderect(pelota_parametros["pelota_rect"], jugador_parametros["jugador_rect"]):
        pelota_parametros["pelota_rect"].bottom = jugador_parametros["jugador_rect"].top
        pelota_parametros["sel_col_pelota"] = jugador_parametros["sel_col_jug"] #pasar color a la pelota

        if pelota_parametros["pelota_rect"].midbottom[0] <= jugador_parametros["jugador_rect"].topright[0] and pelota_parametros["pelota_rect"].midbottom[0] >= jugador_parametros["jugador_rect"].midtop[0]:
            if pelota_parametros["vel_x"] < 0:
                pelota_parametros["vel_x"] *= -1

        if pelota_parametros["pelota_rect"].midbottom[0] >= jugador_parametros["jugador_rect"].topleft[0] and pelota_parametros["pelota_rect"].midbottom[0] <= jugador_parametros["jugador_rect"].midtop[0]:
            if pelota_parametros["vel_x"] > 0:
                pelota_parametros["vel_x"] *= -1
        
        rebote.play()
        pelota_parametros["vel_y"] *= -1
    
    #return vel_x, vel_y, vidas, sel_col_pelota
    #return vidas

def cambiar_color_pelota(pelota_parametros):

    """
    cambio del la imagen de la pelota en funcion de su atributo de color

    Arg:
    nueva_imagen : imagen de la pelota
    """
    if pelota_parametros["sel_col_pelota"]  == 0:
        color = PEL_VERDE
    elif pelota_parametros["sel_col_pelota"] == 1:
        color = PEL_AZUL
    elif pelota_parametros["sel_col_pelota"] == 2:
        color = PEL_ROJA
    
    pelota_imagen = pygame.image.load(color).convert_alpha()
    pelota_imagen = pygame.transform.scale_by(pelota_imagen,0.1)
    pelota_parametros["color_actual"] = color
    
    return pelota_imagen
    