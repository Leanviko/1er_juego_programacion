import pygame
import sys
import random
import json
import bloques
import estadisticas
import botones
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
AZUL = configuracion["azul"]
VERDE = configuracion["verde"]

PEL_ROJA = configuracion["pelota_roja"]
PEL_AZUL = configuracion["pelota_azul"]
PEL_VERDE = configuracion["pelota_verde"]
#fuente
fuente = pygame.font.Font("fuentes\AtariClassic.ttf",TAM_FUENTE)


reloj = pygame.time.Clock()


pantalla = pygame.display.set_mode((ANCHO_VENTANA, ALTO_VENTANA))
pygame.display.set_caption("jueguito piola")

iniciar_juego = False
pausa_juego = False
partida_perdida = False

mover_izquierda = False
mover_derecha = False
pos = pygame.mouse.get_pos()

fondo = pygame.image.load("imagenes/fondo_juego.png").convert_alpha()
#botones
boton_iniciar = pygame.image.load("imagenes/botones/button_start.png").convert_alpha()
boton_salir = pygame.image.load("imagenes/botones/button_exit.png").convert_alpha()
boton_reanudar = pygame.image.load("imagenes/botones/button_resume.png").convert_alpha()
boton_reiniciar = pygame.image.load("imagenes/botones/button_restart.png").convert_alpha()
#carteles
cartel_gameover = pygame.image.load("imagenes/carteles/game_over.png").convert_alpha()
game_over_rect = cartel_gameover.get_rect()

sel_col_jug = 0
sel_col_pelota = 2

color_actual = PEL_AZUL
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
vidas = configuracion["vidas"]


jugando = True
while jugando:

    if iniciar_juego == False:
        pantalla.fill(FONDO)
        if botones.crear_boton(pantalla, boton_iniciar, ANCHO_VENTANA//2,ALTO_VENTANA//2,pos) == True:
                iniciar_juego = True
    else:
        if partida_perdida == True:
            game_over_rect.centerx = ANCHO_VENTANA//2
            game_over_rect.centery = ALTO_VENTANA//2
            pantalla.blit(cartel_gameover, game_over_rect)
            #if botones.crear_boton(pantalla, boton_iniciar, ANCHO_VENTANA//2,ALTO_VENTANA//2,pos) == True:
                    #iniciar_juego = True
        else:
            if pausa_juego == True:
                if botones.crear_boton(pantalla, boton_reanudar, ANCHO_VENTANA//2,ALTO_VENTANA//2,pos):
                    pausa_juego = False
            else:

                pantalla.blit(fondo, (0, 0))
                
                if mover_derecha == True:
                    jugador_rect.centerx += VEL_JUGADOR
                if mover_izquierda == True:
                    jugador_rect.centerx -= VEL_JUGADOR

                vel_x, vel_y, vidas, sel_col_pelota = pelota_logica(pelota_rect, jugador_rect, vel_x, vel_y, ANCHO_VENTANA, ALTO_VENTANA, vidas,sel_col_jug,sel_col_pelota)

                vel_y, puntaje = bloques.logica_bloques(esq_bloques, pelota_rect, vel_y, puntaje, sel_col_jug, sel_col_pelota)

                if vidas == 0:
                    partida_perdida = True

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
                    pelota_imagen, color_actual = cambiar_color_pelota(PEL_VERDE)
                elif sel_col_pelota == 1:
                    pelota_imagen, color_actual = cambiar_color_pelota(PEL_AZUL)
                elif sel_col_pelota == 2:
                    pelota_imagen, color_actual = cambiar_color_pelota(PEL_ROJA)

                pantalla.blit(pelota_imagen, pelota_rect)
    
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
                if evento.key == pygame.K_p:
                    if pausa_juego == False:
                        pausa_juego = True
                    else:
                        pausa_juego = False


            if evento.type == pygame.KEYUP:
                if evento.key == pygame.K_a:
                    mover_izquierda = False
                if evento.key == pygame.K_d:
                    mover_derecha = False

    pygame.display.flip()

    reloj.tick(60)