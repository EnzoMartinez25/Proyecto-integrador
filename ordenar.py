from rich.console import Console
from buscar import mostrar_resultados

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
    limpiar_consola()
    console.print("--- 🗂️ ORDENAR PAISES 🗂️ ---", style="bold cyan")

    # --- SELECCION DE CRITERIO ---
    console.print("1 - Por nombre", style="green")
    console.print("2 - Por poblacion", style="green")
    console.print("3 - Por superficie", style="green")
    
    try:
        opcion = int(input("Elige una opcion: "))
    except ValueError:
        console.print("Debe ingresar un numero valido.", style="yellow")
        input("\nPresiona Enter para continuar...")
        return []

    # --- SELECCION DE ORDEN ---
    console.print("4 - Ascendente", style="green")
    console.print("5 - Descendente", style="green")
    try:
        orden = int(input("Elige el orden: "))
        reversa = True if orden == 5 else False
        if orden not in [4,5]:
            console.print("ORDEN NO VALIDO. Se usara ascendente por defecto.", style="yellow")
            reversa = False
    except ValueError:
        console.print("ENTRADA NO VALIDA. Se usara ascendente por defecto.", style="yellow")
        reversa = False

    # --- ORDENAMIENTO SEGUN CRITERIO ---
    if opcion == 1:
        paises_ordenados = sorted(paises, key=obtener_nombre, reverse=reversa)
    elif opcion == 2:
        paises_ordenados = sorted(paises, key=obtener_poblacion, reverse=reversa)
    elif opcion == 3:
        paises_ordenados = sorted(paises, key=obtener_superficie, reverse=reversa)
    else:
        console.print("OPCION INVALIDA ❌", style="red")
        input("\nPresiona Enter para continuar...")
        return []

    # --- MOSTRAR RESULTADOS CON RICH ---
    mostrar_resultados(paises_ordenados)
    input("\nPresiona Enter para continuar...")

    return paises_ordenados