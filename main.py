from colorama import Fore, Style, init
import os

init(autoreset=True)

from cargar import cargar_paises
from buscar import buscar_pais
from filtrar import filtrar_por_continente, filtrar_por_poblacion, filtrar_por_superficie
from ordenar import ordenar_paises
from estadisticas import pais_mayor_poblacion, pais_menor_poblacion, promedio_poblacion, promedio_superficie, cantidad_por_continente


# --- SUBMENU FILTRAR ---

def menu_filtrar(paises):

    while True:
        print(Fore.CYAN + Style.BRIGHT + "--- 🌍 FILTRAR PAISES 🌍---")
        print(Fore.GREEN + "1 - Por continente")
        print(Fore.GREEN + "2 - Por poblacion")
        print(Fore.GREEN + "3 - Por superficie")
        print(Fore.GREEN + "4 - Volver al menu principal")

        opcion = input("Elige una opcion: ").strip()

        if opcion == "1":
            continente = input("Ingresa continente: ")
            resultados = filtrar_por_continente(paises, continente)
            if resultados:
                for pais in resultados:
                    print(pais)
            else:
                print(Fore.YELLOW + "No se encontraron resultados.")

        elif opcion == "2":
            min_pob = input("Poblacion minima: ")
            max_pob = input("Poblacion maxima: ")
            resultados = filtrar_por_poblacion(paises, min_pob, max_pob)
            if resultados:
                for pais in resultados:
                    print(pais)
            else:
                print(Fore.YELLOW + "No se encontraron resultados.")

        elif opcion == "3":
            min_sup = input("Superficie minima: ")
            max_sup = input("Superficie maxima: ")
            resultados = filtrar_por_superficie(paises, min_sup, max_sup)
            if resultados:
                for pais in resultados:
                    print(pais)
            else:
                print(Fore.YELLOW + "No se encontraron resultados.")

        elif opcion == "4":
            break  # aca vuelvee al menu principal

        else:
            print(Fore.RED + "OPCION INVALIDA. INTENTE DE NUEVO ❌")



# --- SUBMENU ESTADISTICAS ---

def menu_estadisticas(paises):
    while True:
        print(Fore.CYAN + Style.BRIGHT + "--- 📊 ESTADISTICAS 📊---")
        print(Fore.GREEN + "1 - Pais con mayor poblacion")
        print(Fore.GREEN + "2 - Pais con menor poblacion")
        print(Fore.GREEN + "3 - Promedio de poblacion")
        print(Fore.GREEN + "4 - Promedio de superficie")
        print(Fore.GREEN + "5 - Cantidad de países por continente")
        print(Fore.GREEN + "6 - Volver al menu principal")

        opcion = input("Elige una opcion: ").strip()

        if opcion == "1":
            mayor = pais_mayor_poblacion(paises)
            if mayor:
                print("Paias con mayor poblacion:", mayor["nombre"], "-", mayor["poblacion"])

        elif opcion == "2":
            menor = pais_menor_poblacion(paises)
            if menor:
                print("Pais con menor poblacion:", menor["nombre"], "-", menor["poblacion"])

        elif opcion == "3":
            print("Promedio de poblacion:", round(promedio_poblacion(paises)))

        elif opcion == "4":
            print("Promedio de superficie:", round(promedio_superficie(paises)))

        elif opcion == "5":
            print("Cantidad de países por continente:", cantidad_por_continente(paises))

        elif opcion == "6":
            break  # se vuelve al menu principal

        else:
            print(Fore.RED + "OPCION INVALIDA. INTENTE DE NUEVO ❌")



# -- MENU PRINCIPAL ---

def menu_principal(paises):

    while True:
        print(Fore.CYAN + Style.BRIGHT + "--- 🌍 MENU PRINCIPAL DE PAISES 🌍---")
        print(Fore.GREEN + "1️⃣  Buscar pais 🔍")
        print(Fore.GREEN + "2️⃣  Filtrar paises 🔦")
        print(Fore.GREEN + "3️⃣  Ordenar paises 🗂️")
        print(Fore.GREEN + "4️⃣  Ver estadisticas 📊")
        print(Fore.GREEN + "5️⃣  Salir 🚪")

        opcion = input("Elige una opcion: ").strip()

        if opcion == "1":
            nombre = input("Ingresa el nombre del pais: ")
            resultados = buscar_pais(paises, nombre)
            if resultados:
                for pais in resultados:
                    print(pais)
            else:
                print(Fore.YELLOW + "No se encontraron resultados.")

        elif opcion == "2":
            menu_filtrar(paises)  # aca llamamos al submenu

        elif opcion == "3":
            ordenar_paises(paises)

        elif opcion == "4":
            menu_estadisticas(paises)  # aca llamamos al sub menu

        elif opcion == "5":
            print("Saliendo")
            break

        else:
            print(Fore.RED + "OPCION INVALIDA. INTENTE DE NUEVO ❌")

# --- FUNCION DEL MAIN PRINCNIPAL ---

def main():
    paises = cargar_paises("paises.csv")
    if not paises:
        print(Fore.YELLOW + "No se pudieron cargar los datos.")
        return
    print("Datos cargados correctamente.")
    menu_principal(paises)

if __name__ == "__main__":
    main()