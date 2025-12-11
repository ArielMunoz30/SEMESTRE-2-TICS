# Función para ingresar temperaturas diarias
def ingresar_temperaturas():
    print("Ingrese las temperaturas de la semana (7 días):")
    temperaturas = []
    for i in range(7):
        temp = float(input(f"Día {i+1}: "))
        temperaturas.append(temp)
    return temperaturas

# Función para calcular el promedio semanal
def calcular_promedio(temps):
    return sum(temps) / len(temps)

# Programa principal
if __name__ == "__main__":
    temps = ingresar_temperaturas()
    promedio = calcular_promedio(temps)
    print(f"\nEl promedio semanal de temperatura es: {promedio:.2f} °C")