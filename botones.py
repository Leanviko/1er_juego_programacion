import pygame

def crear_boton(superficie,imagen, pos_x, pos_y, pos, sonido):
    """
    toma una imagen u la coloca en las coordenadas proporcionadas

    Args:
    -superficie : Superficie donde se colocara el boton
    -imagen(png): imganen del boton 
    -pos_x (int): posicion en x
    -pos_y (int): posicion en y
    -pos (int,int): posicion del mouse
    -sonido (wav): sonido a utilizar 
    """
    accion = False

    imagen_rect = imagen.get_rect()
    imagen_rect.centerx = pos_x
    imagen_rect.centery = pos_y

    pos = pygame.mouse.get_pos()

    if imagen_rect.collidepoint(pos):
        if pygame.mouse.get_pressed()[0]:
            sonido.play()
            accion = True
    
    superficie.blit(imagen,imagen_rect)

    
    return accion

