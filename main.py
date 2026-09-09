import csv

#Function attempts to open and read a CSV file. If it exists, converts each row into a dict and adds it to a list. If it doesn't exist yet, catch the error and return an empty list instead. Function will return a list of dicts (empty or with data)
def cargar_canciones(nombre_archivo):
    canciones = []
    try:
        with open(nombre_archivo, mode="r") as archivo:
            lector = csv.DictReader(archivo)
            for fila in lector:
                canciones.append(fila)
    except FileNotFoundError:
        pass
    return canciones

resultado = cargar_canciones("canciones.csv") #Works
