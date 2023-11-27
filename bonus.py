import pygame




def bonus_logica(pantalla, lista_bonus_imagen, lista_bonus_rect, pelota_rect, lista_bonus, vel_x, vel_y, bonus_estado, vidas, ancho_jugador):
    
    
    try:
        for bonus in lista_bonus:
            if bonus["tipo"] == 1 :
                lista_bonus_rect[0].centerx = bonus["pos_x"]
                lista_bonus_rect[0].centery = bonus["pos_y"]

                pantalla.blit(lista_bonus_imagen[0], lista_bonus_rect[0])
    except IndexError:
        print("Error de indice")

    for bonus in lista_bonus:
        if pygame.Rect.colliderect(pelota_rect, lista_bonus_rect[0]) and bonus_estado == False:
            lista_bonus.remove(bonus)
            tiempo = pygame.time.get_ticks()
            
            ancho_jugador = 0
                #print(tiempo)

                # if bonus_estado == True and (pygame.time.get_ticks() - tiempo > 1000):
                #     vel_x = 6
                #     vel_y = 6
                #     tiempo = pygame.time.get_ticks()
        

    return vel_x, vel_y, vidas, ancho_jugador