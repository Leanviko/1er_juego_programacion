import pygame

def pelota_logica(pelota_rect, jugador_rect, vel_x, vel_y, ancho_ventana, alto_ventana, vidas,sel_col_jug,sel_col_pelota,sonido):
    pelota_rect.centerx += vel_x
    pelota_rect.centery += vel_y

    if pelota_rect.right >= ancho_ventana:
        pelota_rect.right = ancho_ventana
        vel_x *= -1
        sonido.play()
    if  pelota_rect.left <= 0:
        pelota_rect.left = 0
        vel_x *= -1
        sonido.play()
    if pelota_rect.top <= 0:
        pelota_rect.top = 0
        vel_y *= -1
        sonido.play()
    if pelota_rect.top > alto_ventana:
        pelota_rect.midbottom = jugador_rect.midtop
        vidas -= 1
        vel_y *= -1 
    
    if pygame.Rect.colliderect(pelota_rect, jugador_rect):
        pelota_rect.bottom = jugador_rect.top
        sel_col_pelota = sel_col_jug #pasar color a la pelota

        if pelota_rect.midbottom[0] <= jugador_rect.topright[0] and pelota_rect.midbottom[0] >= jugador_rect.midtop[0]:
            if vel_x < 0:
                vel_x *= -1

        if pelota_rect.midbottom[0] >= jugador_rect.topleft[0] and pelota_rect.midbottom[0] <= jugador_rect.midtop[0]:
            if vel_x > 0:
                vel_x *= -1
        sonido.play()
        vel_y *= -1
    
    return vel_x, vel_y, vidas, sel_col_pelota

def cambiar_color_pelota(nueva_imagen):
    
    pelota_imagen = pygame.image.load(nueva_imagen).convert_alpha()
    pelota_imagen = pygame.transform.scale_by(pelota_imagen,0.1)
    color_actual = nueva_imagen
    
    return pelota_imagen, color_actual
    