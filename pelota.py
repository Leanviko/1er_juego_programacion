import pygame

def pelota_logica(pelota_rect, jugador_rect, vel_x, vel_y, ancho_ventana, alto_ventana, vidas):
    pelota_rect.centerx += vel_x
    pelota_rect.centery += vel_y

    if pelota_rect.right >= ancho_ventana:
        pelota_rect.right = ancho_ventana
        vel_x *= -1
    if  pelota_rect.left <= 0:
        pelota_rect.left = 0
        vel_x *= -1
    if pelota_rect.top <= 0:
        pelota_rect.top = 0
        vel_y *= -1
    if pelota_rect.top > alto_ventana:
        pelota_rect.midbottom = jugador_rect.midtop
        vidas -= 1
        vel_y *= -1 
    if pygame.Rect.colliderect(pelota_rect, jugador_rect):
        pelota_rect.bottom = jugador_rect.top
        vel_y *= -1
    
    return vel_x, vel_y, vidas