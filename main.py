import pygame
import sys
import random
import json
import bloques
from pelota import cambiar_color_pelota, pelota_logica
from estadisticas import puntaje_pantalla, vidas_pantalla
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


sel_col_jug = 0
sel_col_pelota = 2
#color_jugador = lista_colores[sel_col_jug]
#color_pelota = lista_colores[sel_col_pelota]




color_actual = 'imagenes/pelota_azul.png'
pelota_imagen = pygame.image.load(color_actual).convert_alpha()
pelota_imagen = pygame.transform.scale_by(pelota_imagen,0.1)
pelota_rect = pelota_imagen.get_rect()

#jugador
jugador_rect = pygame.Rect(ANCHO_VENTANA//2-50,ALTO_VENTANA-50,100,15)
# pelota
pelota_rect.midbottom = jugador_rect.midtop
vel_x = VEL_PELOTA
vel_y = VEL_PELOTA

puntaje = 0
vidas = 5


jugando = True
while jugando:
    print(f"{sel_col_jug} = {sel_col_pelota}")
    pantalla.blit(fondo, (0, 0))
    

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            jugando = False

        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_a:
                mover_izquierda = True
            if evento.key == pygame.K_d:
                mover_derecha = True
            if evento.key == pygame.K_SPACE:
                sel_col_jug +=1
                if sel_col_jug>2:
                    sel_col_jug = 0

        if evento.type == pygame.KEYUP:
            if evento.key == pygame.K_a:
                mover_izquierda = False
            if evento.key == pygame.K_d:
                mover_derecha = False
    
    if mover_derecha == True:
        jugador_rect.centerx += VEL_JUGADOR
    if mover_izquierda == True:
        jugador_rect.centerx -= VEL_JUGADOR
    


    vel_x, vel_y, vidas, sel_col_pelota = pelota_logica(pelota_rect, jugador_rect, vel_x, vel_y, ANCHO_VENTANA, ALTO_VENTANA, vidas,sel_col_jug,sel_col_pelota)

    vel_y, puntaje = bloques.logica_bloques(esq_bloques, pelota_rect, vel_y, puntaje, sel_col_jug, sel_col_pelota)

    puntaje_pantalla(pantalla,fuente, puntaje)
    vidas_pantalla(pantalla,fuente, vidas)

    bloques.dibujado_bloques(pantalla,esq_bloques)
    

    if sel_col_jug == 0:
        pygame.draw.rect(pantalla,(50,200,20),jugador_rect)
    elif sel_col_jug == 1:
        pygame.draw.rect(pantalla,(10,50,200),jugador_rect)
    elif sel_col_jug == 2:
        pygame.draw.rect(pantalla,(200,50,10),jugador_rect)

    if sel_col_pelota == 0:
        pelota_imagen, color_actual = cambiar_color_pelota('imagenes/pelota_verde.png')
    elif sel_col_pelota == 1:
        pelota_imagen, color_actual = cambiar_color_pelota('imagenes/pelota_azul.png')
    elif sel_col_pelota == 2:
        pelota_imagen, color_actual = cambiar_color_pelota('imagenes/pelota_roja.png')
    

    pantalla.blit(pelota_imagen, pelota_rect)

    pygame.display.flip()

    reloj.tick(60)