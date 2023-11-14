import pygame
import sys
import random
import configuracion


pygame.init()

reloj = pygame.time.Clock()

pantalla = pygame.display.set_mode((configuracion.WIDTH, configuracion.HEIGHT))
pygame.display.set_caption("jueguito piola")

jugando = True
while jugando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.flip()

    reloj.tick(60)