# api_paises.py
import requests
import csv
import os

def actualizar_csv_desde_api():
    archivo_csv = "paises.csv"

    # Si ya existe, no se descarga de nuevo
    if os.path.exists(archivo_csv):
        print("El archivo 'paises.csv' ya existe. No se descargara de nuevo.")
        return

    print("Descargando paises desde la API...")
    url = "https://api-paises-zilz.onrender.com/paises"
    
    try:
        response = requests.get(url)
        response.raise_for_status()  # Lanza error si falla la conexion

        data = response.json()  # Lista de paises
        paises = []

        for pais in data:
            try:
                nombre = pais.get("pais", "Desconocido")        
                poblacion = int(pais.get("poblacion", 0))
                superficie = int(pais.get("superficie", 0))
                continente = pais.get("continente", "Desconocido")

                paises.append({
                    "nombre": nombre,
                    "poblacion": poblacion,
                    "superficie": superficie,
                    "continente": continente
                })
            except ValueError:
                print(f"Error en los datos de {pais.get('pais', 'Desconocido')}, se omite este pais.")

        # Guardar CSV
        with open(archivo_csv, "w", newline="", encoding="utf-8") as f:
            campos = ["nombre", "poblacion", "superficie", "continente"]
            writer = csv.DictWriter(f, fieldnames=campos)
            writer.writeheader()
            writer.writerows(paises)

        print("Archivo 'paises.csv' creado correctamente desde la API.")

    except requests.RequestException as e:
        print(f"Error al conectar con la API: {e}")