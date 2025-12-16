# Programa para calcular el promedio semanal de temperaturas

def ingresar_temperaturas():
    temperaturas = [] # Lista para almacenar temperaturas por días de la semana
    print("Ingrese la temperatura de cada día de la semana:")
    for i in range(7): # Iterar por 7 días
        temp = float(input(f" Día {i+1}: ")) # Solicitar temperatura
        temperaturas.append(temp) # Agregar a la lista
    return temperaturas 

def calcular_promedio(temps):
    return sum(temps) / len(temps)

# Función principal
def main():
    temps = ingresar_temperaturas() # Datos obtenidos del teclado en consola
    promedio = calcular_promedio(temps) # Resultado del promedio
    print(f"\nEl promedio semanal de temperatura es: {promedio:.2f} °C")

# Ejecutar
main()
