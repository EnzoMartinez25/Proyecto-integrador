def obtener_nombre(pais):
    return pais["nombre"]

def obtener_poblacion(pais):
    return pais["poblacion"]

def obtener_superficie(pais):
    return pais["superficie"]


def ordenar_paises(paises):
    print("--- ORDENAR PAISES ---")
    print("1 - Por nombre")
    print("2 - Por poblacion")
    print("3 - Por superficie")

    opcion = input("Elige una opcion: ").strip()

    print("4 - Ascendente")
    print("5 - Descendente")

    orden = input("Elige el ordEn: ").strip()

    reversa = False
    if orden == "5":
        reversa = True

    if opcion == "1":
        paises_ordenados = sorted(paises, key=obtener_nombre, reverse=reversa)
    elif opcion == "2":
        paises_ordenados = sorted(paises, key=obtener_poblacion, reverse=reversa)
    elif opcion == "3":
        paises_ordenados = sorted(paises, key=obtener_superficie, reverse=reversa)
    else:
        print("OPCION INVALIDA.")
        return []

    print("Paises ordenados:")
    for pais in paises_ordenados:
        print(f"{pais['nombre']} - Poblacion: {pais['poblacion']:,} - Superficie: {pais['superficie']:,}")

    return paises_ordenados