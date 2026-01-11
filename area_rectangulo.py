"""
Programa: Cálculo del área de un rectángulo
Autor: Robert Reyes
Descripción:
Este programa solicita al usuario el ancho y alto de un rectángulo,
calcula su área y muestra el resultado.
Se utilizan diferentes tipos de datos y buenas prácticas de nomenclatura.

Ejemplo de ejecución:

Ingrese el ancho del rectángulo: 5
Ingrese el alto del rectángulo: 3

--- Resultados ---
Ancho: 5.0
Alto: 3.0
Área del rectángulo: 15.0
¿El área es válida?: True
"""

# Solicitud de datos al usuario (float)
width = float(input("Ingrese el ancho del rectángulo: "))
height = float(input("Ingrese el alto del rectángulo: "))

# Cálculo del área (float)
area = width * height

# Variable de tipo boolean
is_valid = area > 0

# Mostrar resultados
print("\n--- Resultados ---")
print(f"Ancho: {width}")
print(f"Alto: {height}")
print(f"Área del rectángulo: {area}")
print(f"¿El área es válida?: {is_valid}")
