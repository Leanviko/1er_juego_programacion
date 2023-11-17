import pygame

def crear_boton(superficie,imagen, pos_x, pos_y, pos):

    accion = False

    imagen_rect = imagen.get_rect()
    imagen_rect.centerx = pos_x
    imagen_rect.centery = pos_y

    pos = pygame.mouse.get_pos()

    if imagen_rect.collidepoint(pos):
        #print("dentro")
        if pygame.mouse.get_pressed()[0]:
            #print("presionado")
            accion = True
    
    superficie.blit(imagen,imagen_rect)
    #print(accion)
    return accion

