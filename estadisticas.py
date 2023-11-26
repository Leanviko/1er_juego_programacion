import pygame

def puntaje_pantalla(pantalla, fuente, puntaje, record):
    texto_puntaje = fuente.render(f"{puntaje}".zfill(6), True,(0,0,0))
    pantalla.blit(texto_puntaje,(650,50))

    puntaje_mayor = fuente.render(f"record:{record}", True,(0,0,0))
    pantalla.blit(puntaje_mayor,(300,50))

def vidas_pantalla(pantalla, fuente, vidas):
    vidas = fuente.render(f"Vidas: {vidas}", True,(0,0,0))
    pantalla.blit(vidas,(50,50))