import pygame
import random

#def crear_bloques(ancho, altura, cant_x, cant_y,lista):
    # for i in range(cant_x):
    #     for j in range(cant_y):
    #         bloques_x =  i *(ancho+5)
    #         bloques_y =  j *(altura+5)
    #         lista.append(pygame.Rect(bloques_x,bloques_y,ancho,altura))

# def crear_bloques(x_primer_bloque, y_primer_bloque,ancho,altura,separacion_x,separacion_y,lista):
#     pos_x = x_primer_bloque
#     pos_y = y_primer_bloque
    
#     for i in range(10):
#         lista.append(pygame.Rect(pos_x, pos_y, ancho, altura))
#         pos_x += separacion_x
#         pos_y += separacion_y


# def dibujar_bloques(lista,ancho, altura, list_norm, list_esp):
#     for bloque in lista:
#         if bloque["tipo"] == "normal":
#             list_norm.append(pygame.Rect(bloque["pos_x"],bloque["pos_y"],ancho,altura))
#         if bloque["tipo"] == "especial":
#             list_esp.append(pygame.Rect(bloque["pos_x"],bloque["pos_y"],ancho,altura))

def logica_bloques(lista_bloques,pelota_rect,vel_y):
    for bloque in lista_bloques:  
        if bloque["golpes"]>0 and pygame.Rect.colliderect(pelota_rect,bloque["rect"]):
            bloque["golpes"] -= 1
            vel_y *= -1
            break
        if bloque["golpes"] <= 0:
            lista_bloques.remove(bloque)
        
    return vel_y
