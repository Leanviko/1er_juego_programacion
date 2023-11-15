import pygame
import sys
import random
import json
from bloques import logica_bloques
from esquema_bloques import bloques


pygame.init()

with open("configuracion.json","r") as conf:
    configuracion = json.load(conf)

ANCHO_VENTANA = configuracion["ancho"]
ALTO_VENTANA = configuracion["alto"]
FRECUENCIA = configuracion["frecuencia"] 
VEL_JUGADOR = configuracion["velocidad_jugador"]
VEL_PELOTA = configuracion["velocidad_pelota"]


#colores
FONDO = configuracion["fondo_pantalla"]
BLANCO = configuracion["blanco"]
ROJO = configuracion["rojo"]


reloj = pygame.time.Clock()

pantalla = pygame.display.set_mode((ANCHO_VENTANA, ALTO_VENTANA))
pygame.display.set_caption("jueguito piola")


mover_izquierda = False
mover_derecha = False


pelota_imagen = pygame.image.load('imagenes/pelota.png').convert_alpha()
pelota_imagen = pygame.transform.scale_by(pelota_imagen,0.1)
pelota_rect = pelota_imagen.get_rect()

# pelota
pelota_rect.right = 70
pelota_rect.centery = ALTO_VENTANA//2
vel_x = VEL_PELOTA
vel_y = VEL_PELOTA


#jugador
jugador_rect = pygame.Rect(ANCHO_VENTANA//2-300,ALTO_VENTANA-50,100,15)


jugando = True
while jugando:

    pantalla.fill(FONDO)

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            jugando = False

        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_a:
                mover_izquierda = True
            if evento.key == pygame.K_d:
                mover_derecha = True

        if evento.type == pygame.KEYUP:
            if evento.key == pygame.K_a:
                mover_izquierda = False
            if evento.key == pygame.K_d:
                mover_derecha = False
    
    if mover_derecha == True:
        jugador_rect.centerx += VEL_JUGADOR
    if mover_izquierda == True:
        jugador_rect.centerx -= VEL_JUGADOR
    
    pelota_rect.centerx += vel_x
    pelota_rect.centery += vel_y

    if pelota_rect.right >= ANCHO_VENTANA:
        pelota_rect.right = ANCHO_VENTANA
        vel_x *= -1
    if  pelota_rect.left <= 0:
        pelota_rect.left = 0
        vel_x *= -1
    if pelota_rect.top <= 0:
        pelota_rect.top = 0
        vel_y *= -1
    if pelota_rect.top > ALTO_VENTANA:
        pelota_rect.midbottom = jugador_rect.midtop
        vel_y *= -1 
    if pygame.Rect.colliderect(pelota_rect, jugador_rect):
        pelota_rect.bottom = jugador_rect.top
        vel_y *= -1
        

    
    vel_y = logica_bloques(bloques, pelota_rect, vel_y)
    # for bloque in bloques:  
    #     if bloque["golpes"]>0 and pygame.Rect.colliderect(pelota_rect,bloque["rect"]):
    #         bloque["golpes"] -= 1
    #         vel_y *= -1
    #         break
    #     if bloque["golpes"] <= 0:
    #         bloques.remove(bloque)
    
    for bloque in bloques:  
        if bloque["tipo"] == "facil":
            pygame.draw.rect(pantalla, (0,50,200), bloque["rect"])
        elif bloque["tipo"] == "medio":
            pygame.draw.rect(pantalla, (0,200,50), bloque["rect"])
        elif bloque["tipo"] == "dificil":
            pygame.draw.rect(pantalla, (200,10,50), bloque["rect"])





    pantalla.blit(pelota_imagen, pelota_rect)
    pygame.draw.rect(pantalla,(0,0,0),jugador_rect)


    pygame.display.flip()

    reloj.tick(60)