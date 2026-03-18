import tkinter as tk
from tkinter import ttk, messagebox
from tkcalendar import DateEntry  # Necesitas instalar tkcalendar

# Lista para almacenar eventos
eventos = []

# Función para agregar evento
def agregar_evento():
    fecha = entry_fecha.get()
    hora = entry_hora.get()
    descripcion = entry_descripcion.get()

    if fecha and hora and descripcion:
        eventos.append((fecha, hora, descripcion))
        actualizar_lista()
        limpiar_campos()
    else:
        messagebox.showwarning("Campos vacíos", "Por favor completa todos los campos")

# Función para actualizar el TreeView
def actualizar_lista():
    for item in tree.get_children():
        tree.delete(item)

    for evento in eventos:
        tree.insert("", "end", values=evento)

# Función para eliminar evento seleccionado
def eliminar_evento():
    seleccion = tree.selection()
    if seleccion:
        confirmacion = messagebox.askyesno("Confirmar", "¿Eliminar evento seleccionado?")
        if confirmacion:
            item = tree.item(seleccion)
            evento = item['values']
            eventos.remove(tuple(evento))
            actualizar_lista()
    else:
        messagebox.showwarning("Selección", "Selecciona un evento para eliminar")

# Función para limpiar campos
from datetime import date  # agrega esto arriba del código

def limpiar_campos():
    entry_fecha.set_date(date.today())  # pone la fecha actual
    entry_hora.delete(0, tk.END)
    entry_descripcion.delete(0, tk.END)

# Crear ventana principal
ventana = tk.Tk()
ventana.title("Agenda Personal")
ventana.geometry("600x400")

# ===== FRAME LISTA =====
frame_lista = tk.Frame(ventana)
frame_lista.pack(pady=10)

# TreeView
tree = ttk.Treeview(frame_lista, columns=("Fecha", "Hora", "Descripción"), show="headings")
tree.heading("Fecha", text="Fecha")
tree.heading("Hora", text="Hora")
tree.heading("Descripción", text="Descripción")

tree.pack()

# ===== FRAME ENTRADA =====
frame_entrada = tk.Frame(ventana)
frame_entrada.pack(pady=10)

# Labels y Entradas
tk.Label(frame_entrada, text="Fecha:").grid(row=0, column=0, padx=5, pady=5)
entry_fecha = DateEntry(frame_entrada, date_pattern='yyyy-mm-dd')
entry_fecha.grid(row=0, column=1, padx=5, pady=5)

tk.Label(frame_entrada, text="Hora:").grid(row=1, column=0, padx=5, pady=5)
entry_hora = tk.Entry(frame_entrada)
entry_hora.grid(row=1, column=1, padx=5, pady=5)

tk.Label(frame_entrada, text="Descripción:").grid(row=2, column=0, padx=5, pady=5)
entry_descripcion = tk.Entry(frame_entrada)
entry_descripcion.grid(row=2, column=1, padx=5, pady=5)

# ===== FRAME BOTONES =====
frame_botones = tk.Frame(ventana)
frame_botones.pack(pady=10)

btn_agregar = tk.Button(frame_botones, text="Agregar Evento", command=agregar_evento)
btn_agregar.grid(row=0, column=0, padx=10)

btn_eliminar = tk.Button(frame_botones, text="Eliminar Evento", command=eliminar_evento)
btn_eliminar.grid(row=0, column=1, padx=10)

btn_salir = tk.Button(frame_botones, text="Salir", command=ventana.quit)
btn_salir.grid(row=0, column=2, padx=10)

# Ejecutar aplicación
ventana.mainloop()