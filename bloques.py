import pygame
import random

def logica_bloques(lista_bloques, pelota_rect, vel_y, puntaje):
    for bloque in lista_bloques:  
        if bloque["golpes"]>0 and pygame.Rect.colliderect(pelota_rect,bloque["rect"]):
            bloque["golpes"] -= 1
            vel_y *= -1
            break
        if bloque["golpes"] <= 0:
            lista_bloques.remove(bloque)
            puntaje += 100
        
    return vel_y, puntaje

def dibujado_bloques(pantalla, lista_bloques):
    for bloque in lista_bloques:  
        if bloque["golpes"] == 3:
            pygame.draw.rect(pantalla, (200,50,0), bloque["rect"])
        elif bloque["golpes"] == 2:
            pygame.draw.rect(pantalla, (0,20,200), bloque["rect"])
        elif bloque["golpes"] == 1:
            pygame.draw.rect(pantalla, (0,200,50), bloque["rect"])
