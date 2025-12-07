class Persona:
    def __init__(self, nombre, edad):
        self.__nombre = nombre   # atributo privado
        self.__edad = edad

    # Getter
    def get_nombre(self):
        return self.__nombre

    # Setter
    def set_nombre(self, nombre):
        self.__nombre = nombre

    def get_edad(self):
        return self.__edad

    def set_edad(self, edad):
        if edad > 0:
            self.__edad = edad
