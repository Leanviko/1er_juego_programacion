import pygame
import sys
import random
import json
import bloques
from bonus import bonus_logica
import estadisticas
import botones
from pelota import cambiar_color_pelota, pelota_logica
from estadisticas import puntaje_pantalla, vidas_pantalla
from esquema_bloques import esq_bloques
from puntuacion import cargar_puntaje, guardar_puntaje



pygame.init()
pygame.mixer.init()

with open("configuracion.json","r") as conf:
    configuracion = json.load(conf)

ANCHO_VENTANA = configuracion["ancho"]
ALTO_VENTANA = configuracion["alto"]
VEL_JUGADOR = configuracion["velocidad_jugador"]
VEL_PELOTA = configuracion["velocidad_pelota"]
TAM_FUENTE = configuracion["tamano_fuente"]
TAM_FUENTE_TITULO = configuracion["tamano_fuente_titulo"]
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
fuente_titulo = pygame.font.Font("fuentes\AtariClassic.ttf",TAM_FUENTE_TITULO)
fuente = pygame.font.Font("fuentes\AtariClassic.ttf",TAM_FUENTE)

#sonidos

pygame.mixer.music.load('sonidos/musica_fondo.mp3')
pygame.mixer.music.set_volume(0.1)

rebote = pygame.mixer.Sound("sonidos/rebote.wav")
rebote.set_volume(0.1)
game_over = pygame.mixer.Sound("sonidos/game_over.mp3")
game_over.set_volume(0.1)
game_over_sono = False
reloj = pygame.time.Clock()


pantalla = pygame.display.set_mode((ANCHO_VENTANA, ALTO_VENTANA))
pygame.display.set_caption("jueguito piola")

iniciar_juego = False
pausa_juego = False
partida_perdida = False
partida_ganada = False

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
#bonus
bonus_lento = pygame.image.load("imagenes/desventajas/jug_chico.png").convert_alpha()
bonus_lento = pygame.transform.scale_by(bonus_lento, 0.2)
bonus_lento_rect = bonus_lento.get_rect()

lista_bonus_imagen = [bonus_lento]
lista_bonus_rect = [bonus_lento_rect]
lista_bonus=[]
#pelota
sel_col_jug = 0
sel_col_pelota = 2
color_actual = PEL_AZUL
pelota_imagen = pygame.image.load(color_actual).convert_alpha()
pelota_imagen = pygame.transform.scale_by(pelota_imagen,0.1)
pelota_rect = pelota_imagen.get_rect()

#jugador
jugador_rect = pygame.Rect(ANCHO_VENTANA//2-50,ALTO_VENTANA-50,100,15)
# posicion pelota
pelota_rect.midbottom = jugador_rect.midtop

vel_x = VEL_PELOTA
vel_y = VEL_PELOTA

bonus_estado = False
puntaje = 0
vidas = configuracion["vidas"]


pygame.mixer.music.play()

jugando = True
while jugando:

    print(cargar_puntaje())
    if iniciar_juego == False:
        pantalla.fill(FONDO)
        titulo = fuente_titulo.render(f"Arkanoid UTN", True,(10,10,10))
        pantalla.blit(titulo,(220,200))

        if botones.crear_boton(pantalla, boton_iniciar, ANCHO_VENTANA//2,ALTO_VENTANA//2,pos,rebote) == True:
                iniciar_juego = True
    else:
        if partida_perdida == True:
            pygame.mixer.music.stop()
            if game_over_sono == False:
                game_over.play()
                game_over_sono = True

            game_over_rect.centerx = ANCHO_VENTANA//2
            game_over_rect.centery = ALTO_VENTANA//2
            puntaje_text = cargar_puntaje()
            
            puntaje_text = fuente.render(f" Puntaje: {puntaje}", True,(100,100,100))
            pantalla.blit(puntaje_text,(250,400))

            pantalla.blit(cartel_gameover, game_over_rect)
            
        else:
            if pausa_juego == True:
                if botones.crear_boton(pantalla, boton_reanudar, ANCHO_VENTANA//2,ALTO_VENTANA//2,pos,rebote):
                    pausa_juego = False
                #pygame.mixer.music.stop()
            elif partida_ganada == True:
                
                    
                    puntaje_text = cargar_puntaje()
                    if int(puntaje) > int(puntaje_text):
                        guardar_puntaje(puntaje)
                    puntaje_text = fuente.render(f" Puntaje: {puntaje}", True,(100,100,100))
                    pantalla.blit(puntaje_text,(250,400))
                    
                #pygame.mixer.music.stop()
            else:

                pantalla.blit(fondo, (0, 0))
                
                #limites jugador
                if mover_derecha == True and jugador_rect.right <= ANCHO_VENTANA:
                    jugador_rect.centerx += VEL_JUGADOR
                if mover_izquierda == True and jugador_rect.left >= 0:
                    jugador_rect.centerx -= VEL_JUGADOR


                vel_x, vel_y, vidas, sel_col_pelota = pelota_logica(pelota_rect, jugador_rect, vel_x, vel_y, ANCHO_VENTANA, ALTO_VENTANA, vidas,sel_col_jug,sel_col_pelota,rebote)

                vel_y, puntaje = bloques.logica_bloques(esq_bloques, lista_bonus, pelota_rect, vel_y, puntaje, sel_col_jug, sel_col_pelota)

                if vidas == 0:
                    puntaje_text = cargar_puntaje()
                    if int(puntaje) > int(puntaje_text):
                        guardar_puntaje(puntaje)
                    partida_perdida = True

                record = cargar_puntaje()
                puntaje_pantalla(pantalla,fuente, puntaje, record)
                vidas_pantalla(pantalla,fuente, vidas)

                bloques.dibujado_bloques(pantalla,esq_bloques,fuente)
                
                vel_x, vel_y, vidas = bonus_logica(pantalla, lista_bonus_imagen, lista_bonus_rect, pelota_rect, lista_bonus, vel_x, vel_y, bonus_estado, vidas)


                if sel_col_jug == 0:
                    pygame.draw.rect(pantalla,VERDE,jugador_rect)
                elif sel_col_jug == 1:
                    pygame.draw.rect(pantalla,AZUL,jugador_rect)
                elif sel_col_jug == 2:
                    pygame.draw.rect(pantalla,ROJO,jugador_rect)

                if sel_col_pelota == 0:
                    pelota_imagen, color_actual = cambiar_color_pelota(PEL_VERDE)
                elif sel_col_pelota == 1:
                    pelota_imagen, color_actual = cambiar_color_pelota(PEL_AZUL)
                elif sel_col_pelota == 2:
                    pelota_imagen, color_actual = cambiar_color_pelota(PEL_ROJA)

                pantalla.blit(pelota_imagen, pelota_rect)

                if len(esq_bloques)==0:
                    partida_ganada = True                
                
                


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