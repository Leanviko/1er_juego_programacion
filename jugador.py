import pygame



def dibujar_jugador(superficie, color, pos_x, pos_y,alto,ancho):
    pygame.draw.rect(superficie, color, pos_x, pos_y,alto,ancho)

