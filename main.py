import pygame
import sys
import random
import json
import bloques
from bonus import bonus_logica
from jugador import cambiar_tamaño_jugador
import estadisticas
import botones
from pelota import cambiar_color_pelota, pelota_logica
from estadisticas import puntaje_pantalla, vidas_pantalla
from esquema_bloques import esq_bloques
from puntuacion import cargar_puntaje, guardar_puntaje

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
#imagenes pelota
PEL_ROJA = configuracion["pelota_roja"]
PEL_AZUL = configuracion["pelota_azul"]
PEL_VERDE = configuracion["pelota_verde"]


#fuente
fuente_titulo = pygame.font.Font("fuentes\AtariClassic.ttf",TAM_FUENTE_TITULO)
fuente = pygame.font.Font("fuentes\AtariClassic.ttf",TAM_FUENTE)

#sonidos

pygame.mixer.music.load('sonidos/musica_fondo.mp3')
pygame.mixer.music.set_volume(0.5)

rebote = pygame.mixer.Sound("sonidos/rebote.wav")
rebote.set_volume(0.1)
game_over = pygame.mixer.Sound("sonidos/game_over.mp3")
game_over.set_volume(0.5)
victoria = pygame.mixer.Sound("sonidos/victoria.mp3")
victoria.set_volume(0.5)
pausa = pygame.mixer.Sound("sonidos/pausa.mp3")
pausa.set_volume(0.9)
game_over_sono = False
victoria_sono = False
pausa_sono = False

#reloj del juego
reloj = pygame.time.Clock()
tiempo = None


pantalla = pygame.display.set_mode((ANCHO_VENTANA, ALTO_VENTANA))
pygame.display.set_caption("jueguito")


#estados del juego
iniciar_juego = False
pausa_juego = False
partida_perdida = False
partida_ganada = False

#movimiento
mover_izquierda = False
mover_derecha = False

#posicion del mouse
pos = pygame.mouse.get_pos()

# imagenes de fondos
fondo_menu = pygame.image.load("imagenes/fondo_main_menu.jpg").convert_alpha()
fondo = pygame.image.load("imagenes/fondo_juego.png").convert_alpha()
#botones
boton_iniciar = pygame.image.load("imagenes/botones/button_start.png").convert_alpha()
boton_salir = pygame.image.load("imagenes/botones/button_exit.png").convert_alpha()
boton_reanudar = pygame.image.load("imagenes/botones/button_resume.png").convert_alpha()
boton_reiniciar = pygame.image.load("imagenes/botones/button_restart.png").convert_alpha()
#carteles
cartel_gameover = pygame.image.load("imagenes/carteles/game_over.png").convert_alpha()
game_over_rect = cartel_gameover.get_rect()
cartel_ganaste = pygame.image.load("imagenes/carteles/ganaste.png").convert_alpha()
cartel_ganaste = pygame.transform.scale_by(cartel_ganaste, 0.3)
ganaste_rect = cartel_ganaste.get_rect()
#bonus
bonus_corto = pygame.image.load("imagenes/especiales/jug_chico.png").convert_alpha()
bonus_corto = pygame.transform.scale_by(bonus_corto, 0.2)
bonus_corto_rect = bonus_corto.get_rect()

bonus_grande = pygame.image.load("imagenes/especiales/jug_grande.png").convert_alpha()
bonus_grande = pygame.transform.scale_by(bonus_grande, 0.2)
bonus_grande_rect = bonus_corto.get_rect()

#listas de tipos de elementos especiales
lista_bonus_imagen = [bonus_corto, bonus_grande]
lista_bonus_rect = [bonus_corto_rect, bonus_grande_rect]
lista_bonus=[]
lista_objetos_bonus = []

#pelota
sel_col_jug = 1
sel_col_pelota = 2
color_actual = PEL_AZUL
pelota_imagen = pygame.image.load(color_actual).convert_alpha()
pelota_imagen = pygame.transform.scale_by(pelota_imagen,0.1)
pelota_rect = pelota_imagen.get_rect()

#jugador 
jugador_imagen = pygame.image.load("imagenes/jugador/j_azul_largo.png").convert_alpha()
jugador_imagen_escala = pygame.transform.scale_by(jugador_imagen,0.2)
jugador_rect = jugador_imagen_escala.get_rect()
jugador_rect.center = (ANCHO_VENTANA//2-50, ALTO_VENTANA-50)
ancho_jugador = 1 #[1]: ancho [0]: corto

# posicion pelota
pelota_rect.midbottom = jugador_rect.midtop

vel_x = VEL_PELOTA
vel_y = VEL_PELOTA

#puntaje y estadisticas
bonus_estado = False
puntaje = 0
vidas = configuracion["vidas"]


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

                #limites jugador
                if mover_derecha == True and jugador_rect.right <= ANCHO_VENTANA:
                    jugador_rect.centerx += VEL_JUGADOR
                if mover_izquierda == True and jugador_rect.left >= 0:
                    jugador_rect.centerx -= VEL_JUGADOR

                # movimiento pelota
                vel_x, vel_y, vidas, sel_col_pelota = pelota_logica(pelota_rect, jugador_rect, vel_x, vel_y, ANCHO_VENTANA, ALTO_VENTANA, vidas,sel_col_jug,sel_col_pelota,rebote)

                #logica bloques y penalizacion
                vel_y, puntaje = bloques.logica_bloques(esq_bloques, lista_bonus, pelota_rect, vel_y, puntaje, sel_col_pelota)

                vel_x, vel_y, vidas, ancho_jugador, bonus_estado, tiempo = bonus_logica(pantalla, lista_bonus_imagen, lista_bonus_rect, pelota_rect, lista_bonus, vel_x, vel_y, bonus_estado, vidas, ancho_jugador, tiempo)

                #puntaje al perder la partida
                if vidas == 0:
                    puntaje_text = cargar_puntaje()
                    if int(puntaje) > int(puntaje_text):
                        guardar_puntaje(puntaje)
                    partida_perdida = True

                record = cargar_puntaje()
                puntaje_pantalla(pantalla,fuente, puntaje, record)

                #vidas en pantalla
                vidas_pantalla(pantalla,fuente, vidas)

                #dibujo bloques
                bloques.dibujado_bloques(pantalla,esq_bloques,fuente)
                
                #penalizacion jugador pequeño
                jugador_imagen, color_actual = cambiar_tamaño_jugador(sel_col_jug,ancho_jugador)

                if bonus_estado == True and (pygame.time.get_ticks() - tiempo > 5000):
                    ancho_jugador = 1


                jugador_imagen_escala = pygame.transform.scale_by(jugador_imagen,0.2)
                juegador_rect = jugador_imagen_escala.get_rect()

                #cambio de color de la pelota
                if sel_col_pelota == 0:
                    pelota_imagen, color_actual = cambiar_color_pelota(PEL_VERDE)
                elif sel_col_pelota == 1:
                    pelota_imagen, color_actual = cambiar_color_pelota(PEL_AZUL)
                elif sel_col_pelota == 2:
                    pelota_imagen, color_actual = cambiar_color_pelota(PEL_ROJA)

                #dibujado en pantalla de pelota y jugador
                pantalla.blit(pelota_imagen, pelota_rect)
                pantalla.blit(jugador_imagen_escala, jugador_rect)


                #ganar partida cuando la lista de bloques esta vacia
                if len(esq_bloques)== 0:
                    partida_ganada = True                
                
                

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