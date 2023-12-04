import pygame



def puntaje_pantalla(pantalla, fuente, datos_pantalla, record):
    """
    Mostrara el puntaje de la partida y el record en pantalla
    
    Args:
    -pantalla: superficie donde se mostrara el puntaje
    -fuente: fuente utilizada
    -puntaje (int): puntaje de la partida
    -record (int): puntaje record

    """
    puntaje = datos_pantalla["puntaje"]
    texto_puntaje = fuente.render(f"{puntaje}".zfill(6), True,(0,0,0))
    pantalla.blit(texto_puntaje,(650,50))

    puntaje_mayor = fuente.render(f"record:{record}", True,(0,0,0))
    pantalla.blit(puntaje_mayor,(20,560))

def vidas_pantalla(pantalla, fuente, datos_pantalla):
    """
    Mostrara el vidad restantes de la partida 

    Args:
    -pantalla: superficie donde se mostraran las vidas
    -fuente: fuente utilizada
    -vidas (int): vidas restantes de la partida
    """
    vid = datos_pantalla["vidas"]
    vidas = fuente.render(f"Vidas: {vid}", True,(0,0,0))
    pantalla.blit(vidas,(50,50))

def temporizador_pantalla(pantalla, fuente, contador,datos_pantalla):
        temporizador = pygame.time.get_ticks()-contador["contador_inicial"]
        segundos = temporizador//1000
        centesimas = (temporizador%1000)//10
        
        
        if temporizador >= contador["intervalo_contador"] * (contador["cont_intervalos"] + 1):
            datos_pantalla["puntaje"] -= 15
            contador["cont_intervalos"] += 1
            contador["mostrar_descuento"] = True
            contador["momento_desc"] = pygame.time.get_ticks()

            
        if pygame.time.get_ticks() - contador["momento_desc"]  < 1500 and contador["mostrar_descuento"]:
            descuento_text = fuente.render("-15",True,(255,10,0))
            descuento_rect = descuento_text.get_rect(center =(700,90))
            pantalla.blit(descuento_text,descuento_rect)
        else:
            contador["mostrar_descuento"] = False


        
        temporizador_text = fuente.render(f"Tiempo",True,(0,0,0))
        temporizador_rect = temporizador_text.get_rect(center =(400,50))
        centesimas_text = fuente.render(f"{segundos}:{centesimas}",True,(0,0,0))
        centesimas_rect = centesimas_text.get_rect(center =(400,70))

        pantalla.blit(temporizador_text,temporizador_rect)
        pantalla.blit(centesimas_text,centesimas_rect)