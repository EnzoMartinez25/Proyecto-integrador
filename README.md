# Proyecto-integrador
TRABAJO PRACTICO INTEGRADOR - PROGRAMACION 1
*Tecnicatura Tecnologica Nacional*

ESTUDIANTES:

DAMIAN ENZO MARTINEZ 
KEVIN PUCA 


Nombre del programa: Sistema de Gestion de Paises

Este programa permite gestionar información sobre paises utilizando Python. El sistema carga los datos desde un archivo CSV y permite realizar consultas, filtros, ordenamientos y obtener estadisticas clave. Esta diseñado para practicar el uso de listas, diccionarios, funciones, condicionales, bucles, ordenamientos y manejo de archivos CSV.

Funciones principales:

-- Buscar paises por nombre (coincidencia parcial o exacta).

-- Filtrar paises por continente, rango de poblacion o rango de superficie.

--Ordenar paises por nombre, poblacion o superficie (ascendente o descendente).

-- Mostrar estadisticas: país con mayor/m menor poblacion, promedios y cantidad de paises por continente.

Tecnologias utilizadas:

-- Python 3.x

-- Libreria colorama para mejorar la visualizacion en consola

-- Manejo de archivos CSV


1 -- Instrucciones de uso ---

Preparar el archivo CSV:

Debe llamarse paises.csv y tener el siguiente formato:

nombre,poblacion,superficie,continente
Argentina,45376763,2780400,América
Japon,125800000,377975,Asia
Brasil,213993437,8515767,America
Alemania,83149300,357022,Europa
(Un ejemplo con pocos paises)

2 -- EJECUTAMOS EL PROGRAMA PRINCIPAL -- 

Abrimo la terminal y buscamos el archivo: main.py (programa principal)

3 -- NAVEGAMOS EN EL MENU --

Seleccionamos una opcion ingresando el numero correspondiente (algunas opciones con sub menus)

Ejemplo de entrada 
Elige la opcion 1: (elegimos la opcion 1 de --- BUSCAR PAISES ---)
Ingresa el nombre el pais: Argentina

Ejemplo de salida
{'nombre': 'Argentina', 'poblacion': 45376763, 'superficie': 2780400, 'continente': 'América'}
Nos da el resultado deseado 

Ejemplo de entrada
Elige una opcion: 2 (elegimos la opcion 2 de --- FILTRAR PAISES ---)

Ejemplo de salida
Nos muestra el submenu de ---FILTRAR PAISES---
Ejemplo de entrada
Elige una opcion: 1 (elegimos la opcion 1 - Por continente)
Ejemplo de salida
Nos muestra una lista de todos los paises del continente ingresado

Ejemplo de entrada
Elige una opcion: 3 (elegimos la opcion 3 --- ORDENAR PAISES ---)
Ejemplo de salida 
Nos muestra un submenu de ---ORDENAR PAISES ---
Ejemplo de entrada
Elige una opcion: 1 (elegimos la opcion 1 - Por nombre)
Elege una opcion: 4 (elegimos la opcion 4 - Ascendente)

Ejemplo de salida
Nos muestra la lista de paises en orden Ascendente

Ejemplo de entrada
Elige una opcion: 4 (Ingresamos la opcion 4 - ESTADISTICAS)
Ejemplo de salida:
Nos muestra un sub menu de ---ESTADISTICAS---
Ejemplo de entrada
Elige una opcion: 1 (Ingresamos la opcion 1 - Pais con mayor poblacion)
Ejemplo de salida 
Nos muestra el pais con mayor poblacion

4 -- SALIR DEL PROGRAMA PRINCIPAL --

Se elige la opcion "Salir" en el menu principal, da por finalizado el programa ejecutado


