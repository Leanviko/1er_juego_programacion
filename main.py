import pygame
import sys
import random
from assets import *
from estados import *
import json
import bloques
from bonus import *
from jugador import *
import estadisticas
import botones
from pelota import *
from estadisticas import *
from esquema_bloques import *
from puntuacion import *
"""
Juego arkanoid con colores, el objetivo es romper todos los bloques de la pantalla utilizando la bola y haciéndola rebotar 
en una pequeña plataforma que se moverá con el teclado.

movimiento izquierda : tecla 'A'
movimiento derecha : tecla 'D'

Se puede pausar el juego con la tecla 'P'

La originalidad que encontré para este juego es que la bola no rompe los bloques cuyo color no coincide con ella.
El jugador podrá cambiar el color de su plataforma apretada la tecla 'espacio' y la pelota se "contagiará" de ese color
cuando colisione con ella

bloques rojos : 3 impactos
bloques azules : 2 impactos
bloques verdes : 1 impactos


De manera azarosa habrá una desventaja para el jugador que achicara la plataforma, este efecto durará 5 segundos.

El juego guardará el puntaje si rompe el anterior récord

"""

pygame.init()

try:
    pygame.mixer.init()
except:
    print("No se encuentra dispositivo de audio")  

#sonido fondo
pygame.mixer.music.load('sonidos/musica_fondo.mp3')
pygame.mixer.music.set_volume(0.001)

#reloj del juego
reloj = pygame.time.Clock()
tiempo = None

#posicion del mouse
pos = pygame.mouse.get_pos()



#pelota
pelota_parametros = {
    "pelota_imagen":pelota_imagen,
    "pelota_rect":pelota_rect, 
    "vel_x" : VEL_PELOTA , 
    "vel_y": VEL_PELOTA, 
    "color_actual" : PEL_AZUL, 
    "sel_col_pelota" : sel_col_pelota
    }


#jugador 
jugador_parametros = {
    "jugador_imagen" : jugador_imagen, 
    "jugador_rect" : jugador_rect, 
    "jugador_imagen_scalada":jugador_imagen_scalada, 
    "ancho_jugador": ancho_jugador, 
    "sel_col_jug": 1, 
    "centro_x":ANCHO_VENTANA//2-50,
    "centro_y":ALTO_VENTANA-60
    }
jugador_parametros["jugador_rect"].centerx = jugador_parametros["centro_x"]
jugador_parametros["jugador_rect"].centery = jugador_parametros["centro_y"]

# posicion pelota/jugador
pelota_parametros["pelota_rect"].midbottom = jugador_parametros["jugador_rect"].midtop

#bonus
lista_bonus=[]
lista_objetos_bonus = []
bonus_tipos = [
    {"bonus_cort_img":bonus_corto,
    "bonus_cort_rect":bonus_corto_rect,
    "estado_bonus": False},
    {"bonus_grand_img":bonus_grande,
    "bonus_grand_rect":bonus_grande_rect,
    "estado_bonus": False}]

#puntaje y estadisticas
datos_pantalla = {"vidas":vidas,"puntaje":puntaje}
bonus_parametros = {"vel_x" : VEL_PELOTA }

pygame.mixer.music.play()

jugando = True
while jugando:

    #Menu principal
    if iniciar_juego == False:
        #pantalla.fill(FONDO)
        pantalla.blit(fondo_menu, (0, 0))

        titulo = fuente_titulo.render(f"Arkanoid UTN", True,(10,10,10))
        pantalla.blit(titulo,(220,200))

        if botones.crear_boton(pantalla, boton_iniciar, ANCHO_VENTANA//2,ALTO_VENTANA//2,pos,rebote) == True:
                iniciar_juego = True
        if botones.crear_boton(pantalla, boton_salir, ANCHO_VENTANA//2,ALTO_VENTANA//2 + 100,pos,rebote) == True:
                jugando = False
    else:
        #Pantalla Game over
        if partida_perdida == True:
            pygame.mixer.music.stop()
            if game_over_sono == False:

                #1er try 
                try:
                    game_over.play()
                except FileNotFoundError:
                    print("no existe el audio")
                game_over_sono = True

            game_over_rect.centerx = ANCHO_VENTANA//2
            game_over_rect.centery = ALTO_VENTANA//2
            puntaje_text = cargar_puntaje()
            
            puntaje_text = fuente.render(f" Puntaje: {puntaje}", True,(100,100,100))
            pantalla.blit(puntaje_text,(250,400))

            pantalla.blit(cartel_gameover, game_over_rect)
            
        else:
            #Pantalla partida en pausa
            if pausa_juego == True:
                pygame.mixer.music.pause()
                
                if pausa_sono == False:
                    pausa.play()
                    pausa_sono = True
                
                if botones.crear_boton(pantalla, boton_reanudar, ANCHO_VENTANA//2,ALTO_VENTANA//2,pos,rebote):
                    pausa_juego = False
            
            # Pantalla de partida ganada
            elif partida_ganada == True:
                    pygame.mixer.music.stop()
                    if victoria_sono == False:
                        victoria.play()
                        victoria_sono = True
                    
                    ganaste_rect.centerx = ANCHO_VENTANA//2
                    ganaste_rect.centery = ALTO_VENTANA//2
                    pantalla.blit(cartel_ganaste, ganaste_rect)

                    puntaje_text = cargar_puntaje()
                    if int(puntaje) > int(puntaje_text):
                        guardar_puntaje(puntaje)
                    puntaje_text = fuente.render(f" Puntaje: {puntaje}", True,(100,100,100))
                    pantalla.blit(puntaje_text,(250,400))
                    
            else:

                # Loop Juego
                if pausa_sono == True:
                    pausa_sono = False
                    pygame.mixer.music.unpause()

                pantalla.blit(fondo, (0, 0))
                
                # temporizador = pygame.time.get_ticks()-contador_inicial
                # segundos = temporizador//1000
                # centesimas = (temporizador%1000)//10
                

                movimiento_jugador(jugador_parametros,mover_derecha,mover_izquierda, VEL_JUGADOR, ANCHO_VENTANA)

                # movimiento pelota
                pelota_logica(pelota_parametros, jugador_parametros, ANCHO_VENTANA, ALTO_VENTANA, datos_pantalla ,rebote)

                #logica bloques y penalizacion
                puntaje = bloques.logica_bloques(esq_bloques, lista_bonus, puntaje, pelota_parametros)
                vidas, tiempo = bonus_logica(pantalla,lista_bonus, bonus_tipos, pelota_parametros, vidas,jugador_parametros, tiempo)

                #puntaje al perder la partida
                if datos_pantalla["vidas"] == 0:
                    puntaje_text = cargar_puntaje()
                    if int(puntaje) > int(puntaje_text):
                        guardar_puntaje(puntaje)
                    partida_perdida = True
                #ganar partida cuando la lista de bloques esta vacia
                if len(esq_bloques)== 0:
                    partida_ganada = True     

                record = cargar_puntaje()
                puntaje_pantalla(pantalla,fuente, datos_pantalla, record)
                #vidas en pantalla
                vidas_pantalla(pantalla,fuente, datos_pantalla)
                #dibujo bloques
                
                #temporizador
                temporizador_pantalla(pantalla, fuente, contador_inicial)

                bloques.dibujado_bloques(pantalla,esq_bloques,fuente)
                #penalizacion jugador pequeño
                cambiar_tamaño_jugador(jugador_parametros)

                pelota_imagen = cambiar_color_pelota(pelota_parametros)

                #dibujado en pantalla de pelota y jugador
                pantalla.blit(pelota_imagen, pelota_rect)
                pantalla.blit(jugador_parametros["jugador_imagen_scalada"], jugador_parametros["jugador_rect"])



    #eventos

    for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                jugando = False

            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_a:
                        mover_izquierda = True
                if evento.key == pygame.K_d:
                        mover_derecha = True
                if evento.key == pygame.K_SPACE:
                    jugador_parametros["sel_col_jug"] += 1
                    if jugador_parametros["sel_col_jug"]>2:
                        jugador_parametros["sel_col_jug"] = 0
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