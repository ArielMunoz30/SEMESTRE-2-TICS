# Importamos la librería Tkinter
import tkinter as tk
from tkinter import messagebox

# -------------------------------
# Funciones de la aplicación
# -------------------------------

def agregar_tarea(event=None):
    """
    Función para agregar una nueva tarea a la lista.
    También se ejecuta cuando el usuario presiona Enter.
    """
    tarea = entrada_tarea.get()  # Obtener texto del Entry

    if tarea != "":
        lista_tareas.insert(tk.END, tarea)  # Agregar a la lista
        entrada_tarea.delete(0, tk.END)     # Limpiar campo de texto
    else:
        messagebox.showwarning("Advertencia", "Escribe una tarea primero")


def marcar_completada():
    """
    Marca la tarea seleccionada como completada.
    Cambia visualmente el texto.
    """
    try:
        indice = lista_tareas.curselection()[0]  # Obtener índice seleccionado
        tarea = lista_tareas.get(indice)

        # Verificar si ya está completada
        if not tarea.startswith("✔ "):
            lista_tareas.delete(indice)
            lista_tareas.insert(indice, "✔ " + tarea)
        else:
            messagebox.showinfo("Info", "La tarea ya está completada")

    except:
        messagebox.showwarning("Advertencia", "Selecciona una tarea")


def eliminar_tarea():
    """
    Elimina la tarea seleccionada de la lista.
    """
    try:
        indice = lista_tareas.curselection()[0]
        lista_tareas.delete(indice)
    except:
        messagebox.showwarning("Advertencia", "Selecciona una tarea para eliminar")


def doble_click(event):
    """
    Evento opcional: marcar tarea como completada con doble clic.
    """
    marcar_completada()


# -------------------------------
# Configuración de la ventana
# -------------------------------

ventana = tk.Tk()
ventana.title("Lista de Tareas")
ventana.geometry("400x400")

# -------------------------------
# Componentes de la interfaz
# -------------------------------

# Campo de entrada
entrada_tarea = tk.Entry(ventana, width=40)
entrada_tarea.pack(pady=10)

# Evento: presionar Enter para agregar tarea
entrada_tarea.bind("<Return>", agregar_tarea)

# Lista de tareas
lista_tareas = tk.Listbox(ventana, width=50, height=15)
lista_tareas.pack(pady=10)

# Evento opcional: doble clic
lista_tareas.bind("<Double-Button-1>", doble_click)

# Botones
boton_agregar = tk.Button(ventana, text="Añadir Tarea", command=agregar_tarea)
boton_agregar.pack(pady=5)

boton_completar = tk.Button(ventana, text="Marcar como Completada", command=marcar_completada)
boton_completar.pack(pady=5)

boton_eliminar = tk.Button(ventana, text="Eliminar Tarea", command=eliminar_tarea)
boton_eliminar.pack(pady=5)

# -------------------------------
# Ejecutar la aplicación
# -------------------------------

ventana.mainloop()