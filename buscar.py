def buscar_pais(paises, nombre_buscar):
    """
    Busca países que contengan 'nombre_buscar' en su nombre (coincidencia parcial o exacta)
    Devuelve una lista de diccionarios con los resultados
    paises proviene del csv prueba que creamos nosotros(paises.csv)
    """
    resultados = []
    nombre_buscar = nombre_buscar.lower().strip()
    
    for pais in paises:
        if nombre_buscar in pais["nombre"].lower():
            resultados.append(pais)
    return resultados