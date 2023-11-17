import csv

def guardar_puntaje(puntaje):
    with open("puntuacion.csv","w", newline='') as archivo:
        writer = csv.writer(archivo)
        writer.writerow(["Puntaje"])
        writer.writerow([puntaje])

def cargar_puntaje():
    try:
        with open("puntuacion.csv","r") as archivo:
            lectura = csv.reader(archivo)
            next(lectura)
            puntaje = int(next(lectura)[0])
            return puntaje
    except FileNotFoundError:
        print("error")