import pygame

def puntaje_pantalla(pantalla, fuente, puntaje):
    texto_puntaje = fuente.render(f"{puntaje}".zfill(6), True,(0,0,0))
    pantalla.blit(texto_puntaje,(650,50))

def vidas_pantalla(pantalla, fuente, vidas):
    texto_puntaje = fuente.render(f"{vidas}", True,(0,0,0))
    pantalla.blit(texto_puntaje,(50,50))