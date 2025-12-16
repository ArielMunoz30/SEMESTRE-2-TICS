# Clase Producto
# Representa un producto que se vende en la tienda
class Producto:
    def __init__(self, nombre, precio, stock):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

    def mostrar_info(self):
        return f"Producto: {self.nombre}, Precio: ${self.precio}, Stock: {self.stock}"

    def reducir_stock(self, cantidad):
        if cantidad <= self.stock:
            self.stock -= cantidad
            return True
        else:
            return False


# Clase Cliente
# Representa a un cliente que realiza compras
class Cliente:
    def __init__(self, nombre):
        self.nombre = nombre
        self.total_compra = 0

    def comprar(self, producto, cantidad):
        if producto.reducir_stock(cantidad):
            costo = producto.precio * cantidad
            self.total_compra += costo
            print(f"{self.nombre} compró {cantidad} unidades de {producto.nombre}")
        else:
            print("No hay suficiente stock disponible")

    def mostrar_total(self):
        print(f"Total a pagar por {self.nombre}: ${self.total_compra}")


# Clase Tienda
# Gestiona los productos disponibles
class Tienda:
    def __init__(self, nombre):
        self.nombre = nombre
        self.productos = []

    def agregar_producto(self, producto):
        self.productos.append(producto)

    def mostrar_productos(self):
        print(f"Productos disponibles en {self.nombre}:")
        for producto in self.productos:
            print(producto.mostrar_info())


# -------- PROGRAMA PRINCIPAL --------

# Crear tienda
tienda = Tienda("Tienda Central")

# Crear productos
producto1 = Producto("Laptop", 800, 5)
producto2 = Producto("Mouse", 20, 10)

# Agregar productos a la tienda
tienda.agregar_producto(producto1)
tienda.agregar_producto(producto2)

# Mostrar productos
tienda.mostrar_productos()

# Crear cliente
cliente = Cliente("Juan")

# Cliente realiza compras
cliente.comprar(producto1, 1)
cliente.comprar(producto2, 2)

# Mostrar total de la compra
cliente.mostrar_total()

# Mostrar stock actualizado
tienda.mostrar_productos()
