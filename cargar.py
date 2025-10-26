import csv

def cargar_paises(nombre_archivo):
    paises = []
    try:
        with open(nombre_archivo, newline='', encoding='utf-8') as csvfile:
            lector = csv.DictReader(csvfile)
            for fila in lector:
                try:
                    pais = {
                        "nombre": fila["nombre"],
                        "poblacion": int(fila["poblacion"]),
                        "superficie": int(fila["superficie"]),
                        "continente": fila["continente"]
                    }
                    paises.append(pais)
                except ValueError:
                    print(f"Error en los datos de {fila['nombre']}, se omite este pais.")
    except FileNotFoundError:
        print("No se encontro el archivo")
    return paises