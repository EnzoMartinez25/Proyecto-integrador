def filtrar_por_continente(paises, continente):
    resultados = []
    try:
        continente = continente.strip().lower()
        if not continente:
            raise ValueError("No ingresaste ningun continente.")

        for pais in paises:
            if continente in pais["continente"].lower():  # coincidencia parcial
                resultados.append(pais)

    except ValueError as e:
        print("Error:", e)
    except Exception as e:
        print("ERROR, Ocurrio un error inesperado:", e)

    return resultados

def filtrar_por_poblacion(paises, min_poblacion, max_poblacion):
    resultados = []
    try:
        min_poblacion = int(min_poblacion)
        max_poblacion = int(max_poblacion)

        if min_poblacion > max_poblacion:
            raise ValueError("El valor mínimo no puede ser mayor que el máximo.")

        for pais in paises:
            if min_poblacion <= pais["poblacion"] <= max_poblacion:
                resultados.append(pais)

    except ValueError:
        print("Error: Debes ingresar números enteros para población mínima y máxima.")
    except Exception as e:
        print("ERROR, Ocurrio un error inesperado:", e)

    return resultados

def filtrar_por_superficie(paises, min_superficie, max_superficie):
    resultados = []
    try:
        min_superficie = int(min_superficie)
        max_superficie = int(max_superficie)

        if min_superficie > max_superficie:
            raise ValueError("El valor mínimo no puede ser mayor que el máximo.")

        for pais in paises:
            if min_superficie <= pais["superficie"] <= max_superficie:
                resultados.append(pais)

    except ValueError:
        print("Error: Debes ingresar números enteros para superficie mínima y máxima.")
    except Exception as e:
        print("ERROR, Ocurrio un error inesperado:", e)

    return resultados

# --- TEST MANUAL DE FILTRAR ---
if __name__ == "__main__":
    paises_test = [
        {"nombre": "Argentina", "poblacion": 45851378, "superficie": 2736690, "continente": "America"},
        {"nombre": "Brasil", "poblacion": 213993437, "superficie": 8515767, "continente": "America"},
        {"nombre": "Alemania", "poblacion": 83240525, "superficie": 357022, "continente": "Europa"},
        {"nombre": "España", "poblacion": 47351567, "superficie": 505990, "continente": "Europa"},
        {"nombre": "Egipto", "poblacion": 110990103, "superficie": 1002450, "continente": "Africa"},
    ]

    print("Test de filtrar_por_continente:")
    resultados = filtrar_por_continente(paises_test, "europ")
    for p in resultados:
        print(f"{p['nombre']} - {p['continente']}")

    print("\nTest de filtrar_por_poblacion (50M a 120M):")
    resultados = filtrar_por_poblacion(paises_test, 50000000, 120000000)
    for p in resultados:
        print(f"{p['nombre']} - {p['poblacion']:,}")

    print("\nTest de filtrar_por_superficie (500000 a 3000000):")
    resultados = filtrar_por_superficie(paises_test, 500000, 3000000)
    for p in resultados:
        print(f"{p['nombre']} - {p['superficie']:,}")
