"""Programa: Cálculo del área de un rectángulo
Descripción:
Este programa solicita al usuario el ancho y el alto de un rectángulo, que serían los datos y posterior va a
calcular su área y determinará si el área es considerada grande.
"""

# Solicitar datos al usuario
ancho_rectangulo = float(input("Ingrese el ancho del rectángulo en metros: "))
alto_rectangulo = float(input("Ingrese el alto del rectángulo en metros: "))

# Cálculo del área
area_rectangulo = ancho_rectangulo * alto_rectangulo

# Determinar si el área es grande (mayor a 50 m²)
area_grande = area_rectangulo > 50

# Mostrar resultados
print("\n--- RESULTADOS ---")
print(f"Ancho: {ancho_rectangulo} m")
print(f"Alto: {alto_rectangulo} m")
print(f"Área del rectángulo: {area_rectangulo} m²")

if area_grande:
    print("El área del rectángulo es grande.")
else:
    print("El área del rectángulo es pequeña.")
