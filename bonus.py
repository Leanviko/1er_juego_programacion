import pygame




def bonus_logica(pantalla,lista_bonus, bonus_tipos, pelota_parametros, vidas,jugador_parametros, tiempo):

    """
        
        bonus_logica(pantalla, lista_bonus_imagen, lista_bonus_rect, pelota_rect, lista_bonus, vel_x, vel_y, bonus_estado, vidas, ancho_jugador, tiempo)
    Logica de los elementos especiales, el tiempo en que aparecen y el efecto sobre el jugador
    
    Args:
    -pantalla : superficie donde estara dibujado el elemento
    -lista_bonus_imagen: lista de imagenes
    -lista_bonus_rect: lista de rectangulos del bonus
    -pelota_rect: rectangulo de la pelota
    -lista_bonus: lista de tipo de bonus
    -vel_x (int): velocidad de la pelota en x
    -vel_y (int): velocidad de la pelota en y
    -bonus_estado (bool): determina si ele elemento fue tomado
    -vidas (int): numero de vidas restantes
    -ancho_jugador (int): largo del jugador

    """
    
    
    #2do try

    try:
        for bonus in lista_bonus:
            if bonus["tipo"] == 1 :

                bonus_tipos[0]["bonus_cort_rect"].centerx = bonus["pos_x"]
                bonus_tipos[0]["bonus_cort_rect"].centery = bonus["pos_y"]

                pantalla.blit(bonus_tipos[0]["bonus_cort_img"], bonus_tipos[0]["bonus_cort_rect"])

    except IndexError:
        print("Error de indice")

    for bonus in lista_bonus:
        if pygame.Rect.colliderect(pelota_parametros["pelota_rect"], bonus_tipos[0]["bonus_cort_rect"]):
            lista_bonus.remove(bonus)
            jugador_parametros["ancho_jugador"] = 0
            bonus_tipos[0]["estado_bonus"] = True
            tiempo = pygame.time.get_ticks()

    if bonus_tipos[0]["estado_bonus"] == True and (pygame.time.get_ticks() - tiempo > 5000):
        jugador_parametros["ancho_jugador"] = 1
        bonus_tipos[0]["estado_bonus"] = False


        

    #return vel_x, vel_y, vidas, ancho_jugador, bonus_estado, tiempo
    return tiempo