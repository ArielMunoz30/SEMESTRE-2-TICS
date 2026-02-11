# inventario.py

from producto import Producto

class Inventario:
    """
    Clase que gestiona una lista de productos.
    """

    def __init__(self):
        self.productos = []  # Lista que almacena objetos Producto

    # ==========================
    # Añadir producto
    # ==========================

    def agregar_producto(self, producto):
        # Verificamos que el ID sea único
        for p in self.productos:
            if p.get_id() == producto.get_id():
                print("❌ Error: Ya existe un producto con ese ID.")
                return
        self.productos.append(producto)
        print("✅ Producto agregado correctamente.")

    # ==========================
    # Eliminar producto
    # ==========================

    def eliminar_producto(self, id_producto):
        for p in self.productos:
            if p.get_id() == id_producto:
                self.productos.remove(p)
                print("✅ Producto eliminado correctamente.")
                return
        print("❌ Producto no encontrado.")

    # ==========================
    # Actualizar producto
    # ==========================

    def actualizar_producto(self, id_producto, nueva_cantidad=None, nuevo_precio=None):
        for p in self.productos:
            if p.get_id() == id_producto:
                if nueva_cantidad is not None:
                    p.set_cantidad(nueva_cantidad)
                if nuevo_precio is not None:
                    p.set_precio(nuevo_precio)
                print("✅ Producto actualizado correctamente.")
                return
        print("❌ Producto no encontrado.")

    # ==========================
    # Buscar por nombre
    # ==========================

    def buscar_por_nombre(self, nombre):
        resultados = []
        for p in self.productos:
            if nombre.lower() in p.get_nombre().lower():
                resultados.append(p)

        if resultados:
            for r in resultados:
                print(r)
        else:
            print("❌ No se encontraron productos con ese nombre.")

    # ==========================
    # Mostrar todos
    # ==========================

    def mostrar_productos(self):
        if not self.productos:
            print("⚠️ El inventario está vacío.")
        else:
            for p in self.productos:
                print(p)
