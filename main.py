from colorama import Fore, Style, init
from rich.console import Console
from rich.table import Table
import os

# Inicializar librerias
init(autoreset=True)
console = Console()

# --- IMPORTS DE FUNCIONES DEL PROYECTO ---
from api_paises import actualizar_csv_desde_api
from cargar import cargar_paises
from buscar import buscar_pais, mostrar_resultados
from filtrar import filtrar_por_continente, filtrar_por_poblacion, filtrar_por_superficie
from ordenar import ordenar_paises
from estadisticas import pais_mayor_poblacion, pais_menor_poblacion, promedio_poblacion, promedio_superficie, cantidad_por_continente

# --- FUNCION PARA LIMPIAR CONSOLA ---
def limpiar_consola():
    console.clear()

# --- SUBMENU FILTRAR ---
def menu_filtrar(paises):
    while True:
        limpiar_consola()
        console.print("--- 🌍 FILTRAR PAISES 🌍 ---", style="bold cyan")
        console.print("1 - Por continente", style="green")
        console.print("2 - Por poblacion", style="green")
        console.print("3 - Por superficie", style="green")
        console.print("4 - Volver al menu principal", style="green")

        opcion = input("Elige una opcion: ").strip()

        if opcion == "1":
            continente = input("Ingresa continente: ")
            resultados = filtrar_por_continente(paises, continente)
            mostrar_resultados(resultados)

        elif opcion == "2":
            min_pob = input("Poblacion minima: ")
            max_pob = input("Poblacion maxima: ")
            resultados = filtrar_por_poblacion(paises, min_pob, max_pob)
            # solo mostramos resultados si no hay error
            if resultados is not None:
                mostrar_resultados(resultados)

        elif opcion == "3":
            min_sup = input("Superficie minima: ")
            max_sup = input("Superficie maxima: ")
            resultados = filtrar_por_superficie(paises, min_sup, max_sup)
            if resultados is not None:
                mostrar_resultados(resultados)

        elif opcion == "4":
            break

        else:
            console.print("OPCION INVALIDA. INTENTE DE NUEVO ❌", style="red")
        input("\nPresiona Enter para continuar...")


# --- SUBMENU ESTADISTICAS ---
def menu_estadisticas(paises):
    while True:
        limpiar_consola()
        console.print("--- 📊 ESTADISTICAS 📊 ---", style="bold cyan")
        console.print("1 - Pais con mayor poblacion", style="green")
        console.print("2 - Pais con menor poblacion", style="green")
        console.print("3 - Promedio de poblacion", style="green")
        console.print("4 - Promedio de superficie", style="green")
        console.print("5 - Cantidad de paises por continente", style="green")
        console.print("6 - Volver al menu principal", style="green")

        opcion = input("Elige una opcion: ").strip()

        if opcion == "1":
            mayor = pais_mayor_poblacion(paises)
            if mayor:
                console.print(f"Pais con mayor poblacion: {mayor['nombre']} - {mayor['poblacion']:,}", style="bold green")

        elif opcion == "2":
            menor = pais_menor_poblacion(paises)
            if menor:
                console.print(f"Pais con menor poblacion: {menor['nombre']} - {menor['poblacion']:,}", style="bold green")

        elif opcion == "3":
            console.print(f"Promedio de poblacion: {round(promedio_poblacion(paises)):,}", style="bold green")

        elif opcion == "4":
            console.print(f"Promedio de superficie: {round(promedio_superficie(paises)):,}", style="bold green")

        elif opcion == "5":
            datos = cantidad_por_continente(paises)
            if datos:
                table = Table(title="🌎 Cantidad de paises por continente 🌎", style="cyan")
                table.add_column("Continente", style="magenta", justify="left")
                table.add_column("Cantidad de paises", style="green", justify="right")
                for cont, cant in datos.items():
                    table.add_row(cont, str(cant))
                console.print(table)
            else:
                console.print("No hay datos disponibles.", style="yellow")

        elif opcion == "6":
            break

        else:
            console.print("OPCION INVALIDA. INTENTE DE NUEVO ❌", style="red")

        input("\nPresiona Enter para continuar...")

# --- MENU PRINCIPAL ---
def menu_principal(paises):
    while True:
        limpiar_consola()
        console.print("--- 🌍 MENU PRINCIPAL DE PAISES 🌍 ---", style="bold cyan")
        console.print("1️⃣ Buscar pais 🔍", style="green")
        console.print("2️⃣ Filtrar paises 🔦", style="green")
        console.print("3️⃣ Ordenar paises 🗂️", style="green")
        console.print("4️⃣ Ver estadisticas 📊", style="green")
        console.print("5️⃣ Salir 🚪", style="green")

        opcion = input("Elige una opcion: ").strip()

        if opcion == "1":
            nombre = input("Ingresa el nombre del pais: ")
            resultados = buscar_pais(paises, nombre)
            mostrar_resultados(resultados)
        
        elif opcion == "2":
            menu_filtrar(paises)

        elif opcion == "3":
            ordenar_paises(paises)

        elif opcion == "4":
            menu_estadisticas(paises)

        elif opcion == "5":
            console.print("Saliendo", style="bold cyan")
            break

        else:
            console.print("OPCION INVALIDA. INTENTE DE NUEVO ❌", style="red")
        input("\nPresiona Enter para continuar...")

# --- FUNCION PRINCIPAL ---
def main():
    # 🔹 Generar CSV automáticamente desde la API si no existe
    actualizar_csv_desde_api()

    # 🔹 Cargar países
    paises = cargar_paises("paises.csv")
    if not paises:
        console.print("No se pudieron cargar los datos.", style="yellow")
        return

    console.print(f"Se cargaron {len(paises)} países correctamente desde el CSV.", style="bold green")
    input("\nPresiona Enter para continuar...")
    menu_principal(paises)

if __name__ == "__main__":
    main()
