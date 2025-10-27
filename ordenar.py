from colorama import Fore, Style, init
import os

init(autoreset=True)

def obtener_nombre(pais):
    return pais["nombre"]

def obtener_poblacion(pais):
    return pais["poblacion"]

def obtener_superficie(pais):
    return pais["superficie"]

def ordenar_paises(paises):
    print(Fore.CYAN + Style.BRIGHT + "--- 🗂️ ORDENAR PAISES 🗂️ ---")
    
    # aca hacemos una validacion de la opcion de criterio
    try:
        print(Fore.GREEN + "1 - Por nombre")
        print(Fore.GREEN + "2 - Por poblacion")
        print(Fore.GREEN + "3 - Por superficie")
        opcion = int(input("Elige una opcion: "))
    except ValueError:
        print(Fore.YELLOW + "Debe ingresar un numero valido")
        return []

    # aca hacemos una validacion de orden ascendente/descendente
    try:
        print(Fore.GREEN + "4 - Ascendente")
        print(Fore.GREEN + "5 - Descendente")
        orden = int(input("Elige el orden: "))
        if orden == 5:
            reversa = True
        elif orden == 4:
            reversa = False
        else:
            print(Fore.YELLOW + "ORDEN NO VALIDO. Se usara ascendente por defecto.")
            reversa = False
    except ValueError:
        print(Fore.YELLOW + "ENTRADA NO VALIDA. Se usara ascendente por defecto.")
        reversa = False

    # Ordena segun la opcion

    if opcion == 1:
        paises_ordenados = sorted(paises, key=obtener_nombre, reverse=reversa)
    elif opcion == 2:
        paises_ordenados = sorted(paises, key=obtener_poblacion, reverse=reversa)
    elif opcion == 3:
        paises_ordenados = sorted(paises, key=obtener_superficie, reverse=reversa)
    else:
        print(Fore.RED + "OPCION INVALIDA ❌")
        return []

    # Mostrar resultados
    print("Paises ordenados:")
    for pais in paises_ordenados:
        print(f"{pais['nombre']} - Poblacion: {pais['poblacion']:,} - Superficie: {pais['superficie']:,}")

    return paises_ordenados