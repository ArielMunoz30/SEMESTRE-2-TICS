# Importar librerías necesarias
import tkinter as tk
from tkinter import messagebox

# Crear ventana principal
ventana = tk.Tk()
ventana.title("Gestor de Datos GUI")
ventana.geometry("400x300")

# -----------------------------
# Función para agregar datos
# -----------------------------
def agregar_dato():
    dato = entrada_texto.get()  # Obtener texto del campo

    # Validar que no esté vacío
    if dato == "":
        messagebox.showwarning("Advertencia", "Por favor ingrese un dato")
    else:
        lista_datos.insert(tk.END, dato)  # Agregar a la lista
        entrada_texto.delete(0, tk.END)   # Limpiar campo de texto

# -----------------------------
# Función para limpiar dato seleccionado
# -----------------------------
def limpiar_dato():
    seleccion = lista_datos.curselection()  # Obtener selección

    if seleccion:
        lista_datos.delete(seleccion)  # Eliminar elemento seleccionado
    else:
        messagebox.showinfo("Información", "Seleccione un dato para eliminar")

# -----------------------------
# Componentes de la interfaz
# -----------------------------

# Etiqueta
label = tk.Label(ventana, text="Ingrese un dato:")
label.pack(pady=5)

# Campo de texto
entrada_texto = tk.Entry(ventana, width=30)
entrada_texto.pack(pady=5)

# Botón agregar
boton_agregar = tk.Button(ventana, text="Agregar", command=agregar_dato)
boton_agregar.pack(pady=5)

# Botón limpiar
boton_limpiar = tk.Button(ventana, text="Limpiar seleccionado", command=limpiar_dato)
boton_limpiar.pack(pady=5)

# Etiqueta lista
label_lista = tk.Label(ventana, text="Datos ingresados:")
label_lista.pack(pady=5)

# Lista de datos
lista_datos = tk.Listbox(ventana, width=40, height=10)
lista_datos.pack(pady=5)

# Ejecutar ventana
ventana.mainloop()