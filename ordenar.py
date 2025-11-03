from colorama import Fore, Style, init
from rich.console import Console
import os

init(autoreset=True)
console = Console()

# --- FUNCIONES DE ORDENAMIENTO ---
def obtener_nombre(pais):
    return pais["nombre"]

def obtener_poblacion(pais):
    return pais["poblacion"]

def obtener_superficie(pais):
    return pais["superficie"]

# --- FUNCION PARA LIMPIAR CONSOLA ---
def limpiar_consola():
    console.clear()

# --- MENU ORDENAR PAISES ---
def ordenar_paises(paises):
    limpiar_consola()  # Limpiamos la pantalla al entrar al menu
    print(Fore.CYAN + Style.BRIGHT + "--- 🗂️ ORDENAR PAISES 🗂️ ---")
    
    # aca hacemos la validacion del criterio de orden
    try:
        print(Fore.GREEN + "1 - Por nombre")
        print(Fore.GREEN + "2 - Por poblacion")
        print(Fore.GREEN + "3 - Por superficie")
        opcion = int(input("Elige una opcion: "))
    except ValueError:
        print(Fore.YELLOW + "Debe ingresar un numero valido")
        input("\nPresiona Enter para continuar...")
        return []

    # aca hacemos la validacion del orden ascendente/descendente
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
        input("\nPresiona Enter para continuar...")
        return []

    # Mostrar resultados
    print(Fore.CYAN + Style.BRIGHT + "\nPaises ordenados:")
    for pais in paises_ordenados:
        print(f"{pais['nombre']} - Poblacion: {pais['poblacion']:,} - Superficie: {pais['superficie']:,}")

    input("\nPresiona Enter para continuar...")  # Espera para que el usuario vea los resultados
    return paises_ordenados