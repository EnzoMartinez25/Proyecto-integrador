import csv

# --- Funcion para cargar paises desde CSV ---
def cargar_paises(nombre_archivo):
    paises = []
    try:
        with open(nombre_archivo, newline='', encoding='utf-8') as csvfile:
            lector = csv.DictReader(csvfile)
            for fila in lector:
                # Convertimos poblacion y superficie a enteros
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


# --- TEST MANUAL ---
if __name__ == "__main__":
    print("Iniciando prueba de la funcion cargar_paises()...\n")
    
    archivo_test = "paises.csv"  # Asegurate de que exista o genera uno con api_paises.py
    paises = cargar_paises(archivo_test)
    
    if paises:
        print(f"✅ Test exitoso: Se cargaron {len(paises)} paises.\n")
        # Mostramos los primeros 5 paises como ejemplo
        for pais in paises[:5]:
            print(pais)
    else:
        print("❌ Test fallido: No se cargaron paises.")
