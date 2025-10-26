def filtrar_por_continente(paises, continente):
    """
    Filtra los paises que pertenezcan al continente indicado
    Devuelve una lista de diccionarios con los resultados
    """
    resultados = []
    try:
        # Limpiamos espacios y pasamos a minúsculas
        continente = continente.strip().lower()

        if not continente:
            raise ValueError("No ingresaste ningun continente.")

        # Recorremos la lista de paises
        for pais in paises:
            if pais["continente"].lower() == continente:
                resultados.append(pais)

    except ValueError as e:
        print("Error:", e)
    except Exception as e:
        print("ERROR, Ocurrio un error inesperado:", e)

    return resultados


def filtrar_por_poblacion(paises, min_poblacion, max_poblacion):
    """
    Filtra los paises cuya poblacion este entre min_poblacion y max_poblacion
    Devuelve una lista de diccionarios con los resultados
    """
    resultados = []

    try:
        # Convertimos los valores a enteros
        min_poblacion = int(min_poblacion)
        max_poblacion = int(max_poblacion)

        if min_poblacion > max_poblacion:
            raise ValueError("El valor minimo no puede ser mayor que el maximo.")

        # Recorremos la lista de países
        for pais in paises:
            if pais["poblacion"] >= min_poblacion and pais["poblacion"] <= max_poblacion:
                resultados.append(pais)

    except ValueError as e:
        print("Error:", e)
    except Exception as e:
        print("ERROR, Ocurrio un error inesperado:", e)

    return resultados


def filtrar_por_superficie(paises, min_superficie, max_superficie):
    
    """Filtra los paises cuya superficie este entre min_superficie y max_superficie
    Devuelve una lista de diccionarios con los resultados
    """
    resultados = []

    try:
        # Convertimos los valores a enteros
        min_superficie = int(min_superficie)
        max_superficie = int(max_superficie)

        if min_superficie > max_superficie:
            raise ValueError("El valor minimo no puede ser mayor que el maximo.")

        # Recorremos la lista de países
        for pais in paises:
            sup = pais["superficie"]
            if sup >= min_superficie and sup <= max_superficie:
                resultados.append(pais)

    except ValueError as e:
        print("Error:", e)
    except Exception as e:
        print("ERROR, Ocurrio un error inesperado:", e)

    return resultados