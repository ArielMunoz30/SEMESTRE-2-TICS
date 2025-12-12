# Promedio semanal de temperatura usando POO

class ClimaSemanal:
    def __init__(self):
        # Atributo encapsulado
        self.__temperaturas = [] # Lista para almacenar temperaturas

    def ingresar_temperaturas(self):
        print("Ingrese la temperatura de cada día:")
        for i in range(7): # Iterar por 7 días
            temp = float(input(f" Día {i+1}: "))
            self.__temperaturas.append(temp) # Agregr a la lista

    def calcular_promedio(self):
        return sum(self.__temperaturas) / len(self.__temperaturas)

# Clase hija para demostrar herencia
class ClimaDetalle(ClimaSemanal):
    def mostrar_resultado(self):
        promedio = self.calcular_promedio()
        print(f"\nEl promedio semanal de temperatura es: {promedio:.2f} °C")

# Programa principal
def main():
    clima = ClimaDetalle() # Instancia de la clase que presentará el resultado
    clima.ingresar_temperaturas() # Ejecutar método para registrar datos en la lista
    clima.mostrar_resultado() # Mostrar el promedio

main()
