class ClimaSemanal:
    def __init__(self):
        self.temperaturas = []  # Atributo para almacenar las temperaturas

    def registrar_datos(self):
        print("Ingrese las temperaturas de la semana (7 días):")
        for i in range(7):
            temp = float(input(f"Día {i+1}: "))
            self.temperaturas.append(temp)

    def promedio(self):
        return sum(self.temperaturas) / len(self.temperaturas)

# Programa principal
if __name__ == "__main__":
    clima = ClimaSemanal()
    clima.registrar_datos()
    promedio = clima.promedio()
    print(f"\nEl promedio semanal de temperatura es: {promedio:.2f} °C")