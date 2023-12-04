import pygame
import json

pygame.font.init()
pygame.mixer.init()


with open("configuracion.json","r") as conf:
    configuracion = json.load(conf)

ANCHO_VENTANA = configuracion["ancho"]
ALTO_VENTANA = configuracion["alto"]
VEL_JUGADOR = configuracion["velocidad_jugador"]
VEL_PELOTA = configuracion["velocidad_pelota"]

TAM_FUENTE = configuracion["tamano_fuente"]
TAM_FUENTE_TITULO = configuracion["tamano_fuente_titulo"]
pygame.display.set_caption("jueguito")
pantalla = pygame.display.set_mode((ANCHO_VENTANA, ALTO_VENTANA))
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

puntaje = 0
vidas = configuracion["vidas"]

color_actual = PEL_AZUL


#fuente
fuente_titulo = pygame.font.Font("fuentes\AtariClassic.ttf",TAM_FUENTE_TITULO)
fuente = pygame.font.Font("fuentes\AtariClassic.ttf",TAM_FUENTE)

rebote = pygame.mixer.Sound("sonidos/rebote.wav")
rebote.set_volume(0.1)
game_over = pygame.mixer.Sound("sonidos/game_over.mp3")
game_over.set_volume(0.5)
victoria = pygame.mixer.Sound("sonidos/victoria.mp3")
victoria.set_volume(0.5)
pausa = pygame.mixer.Sound("sonidos/pausa.mp3")
pausa.set_volume(0.9)

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

#pelota
pelota_imagen = pygame.image.load(color_actual).convert_alpha()
pelota_imagen = pygame.transform.scale_by(pelota_imagen,0.1)
pelota_rect = pelota_imagen.get_rect()

#jugador
jugador_imagen = pygame.image.load("imagenes/jugador/j_azul_largo.png").convert_alpha()
jugador_imagen_scalada = pygame.transform.scale_by(jugador_imagen,0.2)
jugador_rect = jugador_imagen_scalada.get_rect()
#jugador_rect.center = (ANCHO_VENTANA//2-50, ALTO_VENTANA-50)