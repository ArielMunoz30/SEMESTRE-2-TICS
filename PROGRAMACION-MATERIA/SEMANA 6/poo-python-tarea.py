# Definición de la clase base Vehiculo
class Vehiculo:
    def __init__(self, marca, modelo, anio):
        # Atributos encapsulados (privados)
        self.__marca = marca
        self.__modelo = modelo
        self.__anio = anio

    # Métodos getters para acceder a los atributos encapsulados
    def get_marca(self):
        return self.__marca

    def get_modelo(self):
        return self.__modelo

    def get_anio(self):
        return self.__anio

    # Método que será sobrescrito (Polimorfismo)
    def descripcion(self):
        return f"Vehículo: {self.__marca} {self.__modelo} del año {self.__anio}"


# Clase derivada Auto que hereda de Vehiculo
class Auto(Vehiculo):
    def __init__(self, marca, modelo, anio, puertas):
        super().__init__(marca, modelo, anio)
        self.puertas = puertas

    # Sobrescritura de método (Polimorfismo)
    def descripcion(self):
        return f"Auto: {self.get_marca()} {self.get_modelo()}, Año {self.get_anio()}, Puertas: {self.puertas}"


# Clase derivada Moto que hereda de Vehiculo
class Moto(Vehiculo):
    def __init__(self, marca, modelo, anio, tipo):
        super().__init__(marca, modelo, anio)
        self.tipo = tipo

    # Sobrescritura de método (Polimorfismo)
    def descripcion(self):
        return f"Moto: {self.get_marca()} {self.get_modelo()}, Año {self.get_anio()}, Tipo: {self.tipo}"


# ----- PROGRAMA PRINCIPAL -----

# Creación de objetos (Definición de Objetos)
vehiculo1 = Auto("Toyota", "Corolla", 2022, 4)
vehiculo2 = Moto("Yamaha", "MT-07", 2021, "Deportiva")

# Uso del polimorfismo
vehiculos = [vehiculo1, vehiculo2]

print("Demostración de Polimorfismo:\n")

for v in vehiculos:
    print(v.descripcion())
