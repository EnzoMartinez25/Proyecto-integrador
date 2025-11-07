# buscar.py
from rich.console import Console
from rich.table import Table

console = Console()

def buscar_pais(paises, nombre_buscar):
    """
    Busca paises que contengan 'nombre_buscar' en su nombre (coincidencia parcial o exacta)
    Devuelve una lista de diccionarios con los resultados
    """
    resultados = []
    nombre_buscar = nombre_buscar.lower().strip()
    
    for pais in paises:
        if nombre_buscar in pais["nombre"].lower():
            resultados.append(pais)
    return resultados

def mostrar_resultados(resultados, pagina_tam=10):
    """
    Muestra los resultados en una tabla con Rich con paginación
    pagina_tam: cantidad de resultados por página
    """
    if not resultados:
        console.print("No se encontraron resultados.", style="yellow")
        return

    total = len(resultados)
    paginas = (total + pagina_tam - 1) // pagina_tam  # calculamos cantidad de páginas

    for i in range(paginas):
        tabla = Table(title=f"Resultados de búsqueda (Página {i+1}/{paginas})", show_lines=True)
        tabla.add_column("Nombre", style="cyan", justify="left")
        tabla.add_column("Población", style="green", justify="right")
        tabla.add_column("Superficie", style="magenta", justify="right")
        tabla.add_column("Continente", style="blue", justify="center")

        inicio = i * pagina_tam
        fin = inicio + pagina_tam
        for pais in resultados[inicio:fin]:
            tabla.add_row(
                pais["nombre"],
                f"{pais['poblacion']:,}",
                f"{pais['superficie']:,}",
                pais["continente"]
            )

        console.print(tabla)
        if i < paginas - 1:
            input("Presiona Enter para ver la siguiente página...")

# --- TEST DEL MODULO DE PRUEBA (opcional) ---
if __name__ == "__main__":
    paises_prueba = [
        {"nombre": "Argentina", "poblacion": 45851378, "superficie": 2736690, "continente": "America"},
        {"nombre": "Brasil", "poblacion": 213993437, "superficie": 8515767, "continente": "America"},
        {"nombre": "Alemania", "poblacion": 83240525, "superficie": 357022, "continente": "Europa"},
        {"nombre": "Armenia", "poblacion": 2963243, "superficie": 29743, "continente": "Asia"},
        {"nombre": "Austria", "poblacion": 9006398, "superficie": 83871, "continente": "Europa"},
        {"nombre": "Aruba", "poblacion": 106766, "superficie": 180, "continente": "America"},
        {"nombre": "Argelia", "poblacion": 44900000, "superficie": 2381741, "continente": "Africa"},
        {"nombre": "Aruba2", "poblacion": 20000, "superficie": 180, "continente": "America"},
        {"nombre": "Aruba3", "poblacion": 20001, "superficie": 180, "continente": "America"},
        {"nombre": "Aruba4", "poblacion": 20002, "superficie": 180, "continente": "America"},
        {"nombre": "Aruba5", "poblacion": 20003, "superficie": 180, "continente": "America"},
    ]

    resultados = buscar_pais(paises_prueba, "ar")
    mostrar_resultados(resultados)

