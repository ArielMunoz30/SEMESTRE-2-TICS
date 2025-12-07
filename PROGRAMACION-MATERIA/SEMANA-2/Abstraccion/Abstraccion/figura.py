from abc import ABC, abstractmethod

class Figura(ABC):

    @abstractmethod
    def calcular_area(self):
        pass

    def mostrar_figura(self):
        print("Soy una figura geométrica.")
