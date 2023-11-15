import pygame
import sys
import random
import json
import bloques
import pelota
from esquema_bloques import esq_bloques


pygame.init()

with open("configuracion.json","r") as conf:
    configuracion = json.load(conf)

ANCHO_VENTANA = configuracion["ancho"]
ALTO_VENTANA = configuracion["alto"]
VEL_JUGADOR = configuracion["velocidad_jugador"]
VEL_PELOTA = configuracion["velocidad_pelota"]
TAM_FUENTE = configuracion["tamano_fuente"]
#colores
FONDO = configuracion["fondo_pantalla"]
BLANCO = configuracion["blanco"]
ROJO = configuracion["rojo"]
#fuente
fuente = pygame.font.Font("fuentes\AtariClassic.ttf",TAM_FUENTE)


reloj = pygame.time.Clock()

pantalla = pygame.display.set_mode((ANCHO_VENTANA, ALTO_VENTANA))
pygame.display.set_caption("jueguito piola")


mover_izquierda = False
mover_derecha = False

fondo = pygame.image.load("imagenes/fondo_juego.png").convert_alpha()
pelota_imagen = pygame.image.load('imagenes/pelota.png').convert_alpha()
pelota_imagen = pygame.transform.scale_by(pelota_imagen,0.1)
pelota_rect = pelota_imagen.get_rect()

#jugador
jugador_rect = pygame.Rect(ANCHO_VENTANA//2-50,ALTO_VENTANA-50,100,15)
# pelota
pelota_rect.midbottom = jugador_rect.midtop
vel_x = VEL_PELOTA
vel_y = VEL_PELOTA



jugando = True
while jugando:

    pantalla.blit(fondo, (0, 0))

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
    


    vel_x, vel_y = pelota.pelota_logica(pelota_rect, jugador_rect, vel_x, vel_y, ANCHO_VENTANA, ALTO_VENTANA)

    vel_y = bloques.logica_bloques(esq_bloques, pelota_rect, vel_y)



    bloques.dibujado_bloques(pantalla,esq_bloques)
    pantalla.blit(pelota_imagen, pelota_rect)

    pygame.draw.rect(pantalla,(0,0,0),jugador_rect)


    pygame.display.flip()

    reloj.tick(60)