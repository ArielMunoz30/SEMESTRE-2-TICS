import json
import os


# =========================
# Clase Producto
# =========================
class Producto:
    def __init__(self, id_producto, nombre, cantidad, precio):
        self.__id = id_producto
        self.__nombre = nombre
        self.__cantidad = cantidad
        self.__precio = precio

    # Métodos getters
    def get_id(self):
        return self.__id

    def get_nombre(self):
        return self.__nombre

    def get_cantidad(self):
        return self.__cantidad

    def get_precio(self):
        return self.__precio

    # Métodos setters
    def set_nombre(self, nombre):
        self.__nombre = nombre

    def set_cantidad(self, cantidad):
        self.__cantidad = cantidad

    def set_precio(self, precio):
        self.__precio = precio

    # Convertir objeto a diccionario (para guardar en archivo)
    def to_dict(self):
        return {
            "id": self.__id,
            "nombre": self.__nombre,
            "cantidad": self.__cantidad,
            "precio": self.__precio
        }

    # Crear objeto desde diccionario
    @staticmethod
    def from_dict(data):
        return Producto(
            data["id"],
            data["nombre"],
            data["cantidad"],
            data["precio"]
        )

    def __str__(self):
        return f"ID: {self.__id} | Nombre: {self.__nombre} | Cantidad: {self.__cantidad} | Precio: ${self.__precio:.2f}"


# =========================
# Clase Inventario
# =========================
class Inventario:
    def __init__(self):
        # Diccionario para almacenar productos
        # Clave: ID del producto
        # Valor: Objeto Producto
        self.productos = {}

    # Añadir producto
    def añadir_producto(self, producto):
        if producto.get_id() in self.productos:
            print("❌ Error: Ya existe un producto con ese ID.")
        else:
            self.productos[producto.get_id()] = producto
            print("✅ Producto añadido correctamente.")

    # Eliminar producto
    def eliminar_producto(self, id_producto):
        if id_producto in self.productos:
            del self.productos[id_producto]
            print("✅ Producto eliminado correctamente.")
        else:
            print("❌ Producto no encontrado.")

    # Actualizar producto
    def actualizar_producto(self, id_producto, cantidad=None, precio=None):
        if id_producto in self.productos:
            if cantidad is not None:
                self.productos[id_producto].set_cantidad(cantidad)
            if precio is not None:
                self.productos[id_producto].set_precio(precio)
            print("✅ Producto actualizado correctamente.")
        else:
            print("❌ Producto no encontrado.")

    # Buscar producto por nombre
    def buscar_por_nombre(self, nombre):
        encontrados = []
        for producto in self.productos.values():
            if nombre.lower() in producto.get_nombre().lower():
                encontrados.append(producto)

        if encontrados:
            for producto in encontrados:
                print(producto)
        else:
            print("❌ No se encontraron productos con ese nombre.")

    # Mostrar todos los productos
    def mostrar_todos(self):
        if not self.productos:
            print("📦 El inventario está vacío.")
        else:
            for producto in self.productos.values():
                print(producto)

    # Guardar inventario en archivo
    def guardar_en_archivo(self, archivo="inventario.json"):
        with open(archivo, "w") as f:
            json.dump(
                {id_producto: prod.to_dict() for id_producto, prod in self.productos.items()},
                f,
                indent=4
            )
        print("💾 Inventario guardado correctamente.")

    # Cargar inventario desde archivo
    def cargar_desde_archivo(self, archivo="inventario.json"):
        if os.path.exists(archivo):
            with open(archivo, "r") as f:
                data = json.load(f)
                for id_producto, prod_data in data.items():
                    self.productos[id_producto] = Producto.from_dict(prod_data)
            print("📂 Inventario cargado correctamente.")
        else:
            print("⚠ No existe archivo de inventario. Se creará uno nuevo.")


# =========================
# Menú Interactivo
# =========================
def menu():
    inventario = Inventario()
    inventario.cargar_desde_archivo()

    while True:
        print("\n===== SISTEMA DE INVENTARIO =====")
        print("1. Añadir producto")
        print("2. Eliminar producto")
        print("3. Actualizar producto")
        print("4. Buscar producto por nombre")
        print("5. Mostrar todos los productos")
        print("6. Guardar inventario")
        print("7. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            id_producto = input("ID: ")
            nombre = input("Nombre: ")
            cantidad = int(input("Cantidad: "))
            precio = float(input("Precio: "))
            producto = Producto(id_producto, nombre, cantidad, precio)
            inventario.añadir_producto(producto)

        elif opcion == "2":
            id_producto = input("Ingrese ID del producto a eliminar: ")
            inventario.eliminar_producto(id_producto)

        elif opcion == "3":
            id_producto = input("Ingrese ID del producto a actualizar: ")
            cantidad = input("Nueva cantidad (dejar vacío si no cambia): ")
            precio = input("Nuevo precio (dejar vacío si no cambia): ")

            cantidad = int(cantidad) if cantidad else None
            precio = float(precio) if precio else None

            inventario.actualizar_producto(id_producto, cantidad, precio)

        elif opcion == "4":
            nombre = input("Ingrese nombre a buscar: ")
            inventario.buscar_por_nombre(nombre)

        elif opcion == "5":
            inventario.mostrar_todos()

        elif opcion == "6":
            inventario.guardar_en_archivo()

        elif opcion == "7":
            inventario.guardar_en_archivo()
            print("👋 Saliendo del sistema...")
            break

        else:
            print("❌ Opción inválida.")


# Ejecutar programa
if __name__ == "__main__":
    menu()
