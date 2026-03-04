# ==========================
# Clase Libro
# ==========================
class Libro:
    def __init__(self, titulo, autor, categoria, isbn):
        self.datos = (titulo, autor)  # Tupla inmutable
        self.categoria = categoria
        self.isbn = isbn

    def __str__(self):
        return f"Título: {self.datos[0]}, Autor: {self.datos[1]}, Categoría: {self.categoria}, ISBN: {self.isbn}"


# ==========================
# Clase Usuario
# ==========================
class Usuario:
    def __init__(self, nombre, id_usuario):
        self.nombre = nombre
        self.id_usuario = id_usuario
        self.libros_prestados = []  # Lista

    def prestar_libro(self, libro):
        self.libros_prestados.append(libro)

    def devolver_libro(self, libro):
        if libro in self.libros_prestados:
            self.libros_prestados.remove(libro)

    def listar_libros(self):
        if not self.libros_prestados:
            print("No tiene libros prestados.")
        else:
            for libro in self.libros_prestados:
                print(libro)


# ==========================
# Clase Biblioteca
# ==========================
class Biblioteca:
    def __init__(self):
        self.libros = {}          # Diccionario
        self.usuarios = {}        # Diccionario
        self.ids_usuarios = set() # Conjunto

    def añadir_libro(self, libro):
        if libro.isbn not in self.libros:
            self.libros[libro.isbn] = libro
            print("Libro añadido correctamente.")
        else:
            print("El libro ya existe.")

    def quitar_libro(self, isbn):
        if isbn in self.libros:
            del self.libros[isbn]
            print("Libro eliminado.")
        else:
            print("Libro no encontrado.")

    def registrar_usuario(self, usuario):
        if usuario.id_usuario not in self.ids_usuarios:
            self.usuarios[usuario.id_usuario] = usuario
            self.ids_usuarios.add(usuario.id_usuario)
            print("Usuario registrado.")
        else:
            print("ID de usuario ya existe.")

    def eliminar_usuario(self, id_usuario):
        if id_usuario in self.ids_usuarios:
            del self.usuarios[id_usuario]
            self.ids_usuarios.remove(id_usuario)
            print("Usuario eliminado.")
        else:
            print("Usuario no encontrado.")

    def prestar_libro(self, isbn, id_usuario):
        if isbn in self.libros and id_usuario in self.usuarios:
            libro = self.libros.pop(isbn)
            usuario = self.usuarios[id_usuario]
            usuario.prestar_libro(libro)
            print("Libro prestado correctamente.")
        else:
            print("Libro o usuario no encontrado.")

    def devolver_libro(self, isbn, id_usuario):
        if id_usuario in self.usuarios:
            usuario = self.usuarios[id_usuario]
            for libro in usuario.libros_prestados:
                if libro.isbn == isbn:
                    usuario.devolver_libro(libro)
                    self.libros[isbn] = libro
                    print("Libro devuelto correctamente.")
                    return
            print("El usuario no tiene ese libro.")
        else:
            print("Usuario no encontrado.")

    def buscar_por_categoria(self, categoria):
        for libro in self.libros.values():
            if libro.categoria.lower() == categoria.lower():
                print(libro)


# ==========================
# PRUEBA DEL SISTEMA
# ==========================

biblio = Biblioteca()

libro1 = Libro("1984", "George Orwell", "Ficción", "111")
libro2 = Libro("Python Básico", "Juan Pérez", "Tecnología", "222")

biblio.añadir_libro(libro1)
biblio.añadir_libro(libro2)

usuario1 = Usuario("Francis", "U001")
biblio.registrar_usuario(usuario1)

biblio.prestar_libro("111", "U001")

print("\nLibros prestados a Francis:")
usuario1.listar_libros()

biblio.devolver_libro("111", "U001")

print("\nBuscar por categoría Tecnología:")
biblio.buscar_por_categoria("Tecnología")