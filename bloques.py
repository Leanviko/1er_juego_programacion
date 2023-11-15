import pygame
import random

def logica_bloques(lista_bloques, pelota_rect, vel_y):
    for bloque in lista_bloques:  
        if bloque["golpes"]>0 and pygame.Rect.colliderect(pelota_rect,bloque["rect"]):
            bloque["golpes"] -= 1
            vel_y *= -1
            break
        if bloque["golpes"] <= 0:
            lista_bloques.remove(bloque)
        
    return vel_y

def dibujado_bloques(pantalla, lista_bloques):
    for bloque in lista_bloques:  
        if bloque["tipo"] == "facil":
            pygame.draw.rect(pantalla, (0,50,200), bloque["rect"])
        elif bloque["tipo"] == "medio":
            pygame.draw.rect(pantalla, (0,200,50), bloque["rect"])
        elif bloque["tipo"] == "dificil":
            pygame.draw.rect(pantalla, (200,10,50), bloque["rect"])
