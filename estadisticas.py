# Funcion auxiliar para obtener poblacion de un pais

def obtener_poblacion(pais):
    return pais["poblacion"]

#   Pais con mayor poblacion

def pais_mayor_poblacion(paises):
    if not paises:
        return None
    
    mayor = paises[0]
    for p in paises:
        if p["poblacion"] > mayor["poblacion"]:
            mayor = p
    return mayor

# Pais con menor poblacion
def pais_menor_poblacion(paises):
    if not paises:
        return None
    
    menor = paises[0]
    for p in paises:
        if p["poblacion"] < menor["poblacion"]:
            menor = p
    return menor

# Promedio de poblacion
def promedio_poblacion(paises):
    if not paises:
        return 0
    total = 0

    for p in paises:
        total += p["poblacion"]
    return total / len(paises)

# Promedio de superficie
def promedio_superficie(paises):
    if not paises:
        return 0
    total = 0

    for p in paises:
        total += p["superficie"]
    return total / len(paises)

# Cantidad de paises por continente

def cantidad_por_continente(paises):
    continentes = {}
    
    for p in paises:
        cont = p["continente"]
        if cont in continentes:
            continentes[cont] += 1
        else:
            continentes[cont] = 1
    return continentes