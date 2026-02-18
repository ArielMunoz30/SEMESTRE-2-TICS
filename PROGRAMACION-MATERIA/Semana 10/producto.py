# producto.py

class Producto:
    """
    Clase que representa un producto dentro del inventario.
    Cada producto tiene un ID único, nombre, cantidad y precio.
    """

    def __init__(self, id_producto, nombre, cantidad, precio):
        # Constructor
        self.__id = id_producto          # Atributo privado
        self.__nombre = nombre
        self.__cantidad = cantidad
        self.__precio = precio

    # =====================
    # Getters
    # =====================

    def get_id(self):
        return self.__id

    def get_nombre(self):
        return self.__nombre

    def get_cantidad(self):
        return self.__cantidad

    def get_precio(self):
        return self.__precio

    # =====================
    # Setters
    # =====================

    def set_nombre(self, nombre):
        self.__nombre = nombre

    def set_cantidad(self, cantidad):
        if cantidad >= 0:
            self.__cantidad = cantidad

    def set_precio(self, precio):
        if precio >= 0:
            self.__precio = precio

    # Método para mostrar información del producto
    def __str__(self):
        return f"ID: {self.__id} | Nombre: {self.__nombre} | Cantidad: {self.__cantidad} | Precio: ${self.__precio:.2f}"
