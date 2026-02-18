# inventario.py

import os
from producto import Producto

class Inventario:
    """
    Clase que gestiona una lista de productos
    y permite almacenamiento persistente en archivo.
    """

    def __init__(self, archivo="inventario.txt"):
        self.archivo = archivo
        self.productos = []
        self.cargar_desde_archivo()

    # ==========================
    # CARGAR INVENTARIO DESDE ARCHIVO
    # ==========================
    def cargar_desde_archivo(self):
        try:
            if not os.path.exists(self.archivo):
                # Si el archivo no existe, se crea automáticamente
                open(self.archivo, "w").close()
                print("📁 Archivo inventario.txt creado automáticamente.")
                return

            with open(self.archivo, "r") as archivo:
                for linea in archivo:
                    try:
                        id_producto, nombre, cantidad, precio = linea.strip().split(",")
                        producto = Producto(
                            id_producto,
                            nombre,
                            int(cantidad),
                            float(precio)
                        )
                        self.productos.append(producto)
                    except ValueError:
                        print("⚠ Línea corrupta encontrada y omitida.")

            print("✅ Inventario cargado correctamente desde archivo.")

        except FileNotFoundError:
            print("❌ Error: Archivo no encontrado.")
        except PermissionError:
            print("❌ Error: No tienes permisos para leer el archivo.")
        except Exception as e:
            print(f"❌ Error inesperado al cargar archivo: {e}")

    # ==========================
    # GUARDAR INVENTARIO EN ARCHIVO
    # ==========================
    def guardar_en_archivo(self):
        try:
            with open(self.archivo, "w") as archivo:
                for p in self.productos:
                    linea = f"{p.get_id()},{p.get_nombre()},{p.get_cantidad()},{p.get_precio()}\n"
                    archivo.write(linea)

            print("💾 Cambios guardados correctamente en inventario.txt.")

        except PermissionError:
            print("❌ Error: No tienes permisos para escribir en el archivo.")
        except Exception as e:
            print(f"❌ Error inesperado al guardar archivo: {e}")

    # ==========================
    # AÑADIR PRODUCTO
    # ==========================
    def agregar_producto(self, producto):
        for p in self.productos:
            if p.get_id() == producto.get_id():
                print("❌ Error: Ya existe un producto con ese ID.")
                return

        self.productos.append(producto)
        self.guardar_en_archivo()
        print("✅ Producto agregado y guardado correctamente.")

    # ==========================
    # ELIMINAR PRODUCTO
    # ==========================
    def eliminar_producto(self, id_producto):
        for p in self.productos:
            if p.get_id() == id_producto:
                self.productos.remove(p)
                self.guardar_en_archivo()
                print("✅ Producto eliminado y archivo actualizado.")
                return

        print("❌ Producto no encontrado.")

    # ==========================
    # ACTUALIZAR PRODUCTO
    # ==========================
    def actualizar_producto(self, id_producto, nueva_cantidad=None, nuevo_precio=None):
        for p in self.productos:
            if p.get_id() == id_producto:

                if nueva_cantidad is not None:
                    p.set_cantidad(nueva_cantidad)

                if nuevo_precio is not None:
                    p.set_precio(nuevo_precio)

                self.guardar_en_archivo()
                print("✅ Producto actualizado y guardado en archivo.")
                return

        print("❌ Producto no encontrado.")

    # ==========================
    # BUSCAR POR NOMBRE
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
    # MOSTRAR TODOS
    # ==========================
    def mostrar_productos(self):
        if not self.productos:
            print("⚠️ El inventario está vacío.")
        else:
            for p in self.productos:
                print(p)
