class Archivo:
    """
    Clase que demuestra el uso de constructor y destructor en Python.
    """
    def __init__(self, nombre_archivo):
        """
        Constructor: se ejecuta automáticamente al crear el objeto.
        Inicializa los atributos y abre un archivo.
        """
        self.nombre_archivo = nombre_archivo
        self.archivo = open(self.nombre_archivo, "w")
        self.archivo.write("Archivo creado usando constructor (__init__)\n")
        print(f"Constructor: Archivo '{self.nombre_archivo}' abierto correctamente.")

    def escribir(self, texto):
        """
        Método para escribir contenido en el archivo.
        """
        self.archivo.write(texto + "\n")
        print("Texto escrito en el archivo.")

    def __del__(self):
        """
        Destructor: se ejecuta automáticamente cuando el objeto
        es eliminado o el programa finaliza.
        Cierra el archivo como limpieza de recursos.
        """
        if not self.archivo.closed:
            self.archivo.write("Destructor ejecutado. Cerrando archivo.\n")
            self.archivo.close()
            print(f"Destructor: Archivo '{self.nombre_archivo}' cerrado correctamente.")


# Programa principal
if __name__ == "__main__":
    archivo1 = Archivo("ejemplo.txt")
    archivo1.escribir("Este es un ejemplo de uso de constructores y destructores.")
    del archivo1  # Fuerza la ejecución del destructor
