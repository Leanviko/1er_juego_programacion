import pygame

def pelota_logica(pelota_parametros, jugador_parametros, ANCHO_VENTANA, ALTO_VENTANA, vidas,rebote):
    """
    
    pelota_logica(pelota_rect, jugador_rect, vel_x, vel_y, ancho_ventana, alto_ventana, vidas,sel_col_jug,sel_col_pelota,sonido)
    
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
    #pelota_parametros["pelota_rect"].centerx += vel_x
    #pelota_parametros["pelota_rect"].centery += vel_y
    
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
        pelota_parametros["pelota_rect"].midbottom = pelota_parametros["pelota_rect"].midtop
        vidas -= 1
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
    return vidas

def cambiar_color_pelota(imagen_color,pelota_parametros):

    """
    cambio del la imagen de la pelota en funcion de su atributo de color

    Arg:
    nueva_imagen : imagen de la pelota
    """
    
    pelota_imagen = pygame.image.load(imagen_color).convert_alpha()
    pelota_imagen = pygame.transform.scale_by(pelota_imagen,0.1)
    pelota_parametros["color_actual"] = imagen_color
    
    return pelota_imagen
    