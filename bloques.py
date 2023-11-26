import pygame
import random
import json

with open("configuracion.json","r") as conf:
    configuracion = json.load(conf)

ROJO = configuracion["rojo"]
AZUL = configuracion["azul"]
VERDE = configuracion["verde"]


def logica_bloques(lista_bloques,lista_bonus, pelota_rect, vel_y, puntaje, sel_col_jug, sel_col_pelota):

    for bloque in lista_bloques:  
        if bloque["golpes"]>0 and pygame.Rect.colliderect(pelota_rect,bloque["rect"]):
            
            if bloque["golpes"] == (sel_col_pelota+1):
                bloque["golpes"] -= 1
                puntaje += 50
            vel_y *= -1
            
            break            
                        
        if bloque["golpes"] <= 0:
            pos_x = bloque["rect"].centerx
            pos_y= bloque["rect"].centery

            puntaje += 100
            bonus = random.randrange(0,10)
            if bonus == 1:
                lista_bonus.append({"tipo":1,"pos_x": pos_x,"pos_y": pos_y})

            lista_bloques.remove(bloque)
        
    return vel_y, puntaje

def dibujado_bloques(pantalla, lista_bloques,fuente):
    for bloque in lista_bloques: 
        golpes = bloque["golpes"]
        texto_golpes = fuente.render(f"{golpes}", True,(255,255,255))
        
        if bloque["golpes"] == 3:
            pygame.draw.rect(pantalla, ROJO, bloque["rect"])
        elif bloque["golpes"] == 2:
            pygame.draw.rect(pantalla, AZUL, bloque["rect"])
        elif bloque["golpes"] == 1:
            pygame.draw.rect(pantalla, VERDE, bloque["rect"])
        
        texto_rect = texto_golpes.get_rect(center=bloque["rect"].center)
        pantalla.blit(texto_golpes,texto_rect)


#     print("golpe costado")
            #     if bloque["rect"].left >= pelota_rect.right:
            #         pelota_rect.right = bloque["rect"].left
            #     else:
            #         pelota_rect.left = bloque["rect"].right
            #     vel_x *= -1
                
            # if bloque["rect"].top <= pelota_rect.bottom or bloque["rect"].bottom >= pelota_rect.top:
            #     #print("golpe arriba/abajo")
            #     if bloque["rect"].bottom >= pelota_rect.top:
            #         pelota_rect.top = bloque["rect"].bottom

            #     elif bloque["rect"].top <= pelota_rect.bottom:
            #         pelota_rect.bottom = bloque["rect"].top

            #     vel_y *= -1