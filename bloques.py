import pygame
import random
import json

with open("configuracion.json","r") as conf:
    configuracion = json.load(conf)

ROJO = configuracion["rojo"]
AZUL = configuracion["azul"]
VERDE = configuracion["verde"]
#colores = {"rojo":1,"azul":2,"verde":3}

def logica_bloques(lista_bloques, pelota_rect, vel_y, puntaje, sel_col_jug, sel_col_pelota):
    for bloque in lista_bloques:  
        if bloque["golpes"]>0 and pygame.Rect.colliderect(pelota_rect,bloque["rect"]):
            
            if bloque["golpes"] == (sel_col_pelota+1):
                bloque["golpes"] -= 1
                vel_y *= -1
                break
            vel_y *= -1
            break
        if bloque["golpes"] <= 0:
            lista_bloques.remove(bloque)
            puntaje += 100
        
    return vel_y, puntaje

def dibujado_bloques(pantalla, lista_bloques):
    for bloque in lista_bloques:  
        if bloque["golpes"] == 3:
            pygame.draw.rect(pantalla, ROJO, bloque["rect"])
        elif bloque["golpes"] == 2:
            pygame.draw.rect(pantalla, AZUL, bloque["rect"])
        elif bloque["golpes"] == 1:
            pygame.draw.rect(pantalla, VERDE, bloque["rect"])
