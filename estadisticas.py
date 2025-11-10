# Funcion para obtener poblacion de un pais

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

# --- TEST MANUAL DE ESTADISTICAS ---
if __name__ == "__main__":
    paises_test = [
        {"nombre": "Argentina", "poblacion": 45851378, "superficie": 2736690, "continente": "America"},
        {"nombre": "Brasil", "poblacion": 213993437, "superficie": 8515767, "continente": "America"},
        {"nombre": "Alemania", "poblacion": 83240525, "superficie": 357022, "continente": "Europa"},
        {"nombre": "España", "poblacion": 47351567, "superficie": 505990, "continente": "Europa"},
        {"nombre": "Egipto", "poblacion": 110990103, "superficie": 1002450, "continente": "Africa"},
    ]

    print("Test de estadisticas:\n")

    mayor = pais_mayor_poblacion(paises_test)
    print(f"Pais con mayor poblacion: {mayor['nombre']} - {mayor['poblacion']:,}")

    menor = pais_menor_poblacion(paises_test)
    print(f"Pais con menor poblacion: {menor['nombre']} - {menor['poblacion']:,}")

    prom_pob = promedio_poblacion(paises_test)
    print(f"Promedio de poblacion: {round(prom_pob):,}")

    prom_sup = promedio_superficie(paises_test)
    print(f"Promedio de superficie: {round(prom_sup):,}")

    por_continente = cantidad_por_continente(paises_test)
    print("Cantidad de paises por continente:")
    for cont, cant in por_continente.items():
        print(f"{cont}: {cant}")
