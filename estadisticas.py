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
    pantalla.blit(puntaje_mayor,(300,50))

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