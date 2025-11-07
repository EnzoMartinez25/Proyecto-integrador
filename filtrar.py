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
