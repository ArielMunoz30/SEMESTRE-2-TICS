import tkinter as tk
from tkinter import messagebox

class AplicacionTareas:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestión de Tareas")
        self.root.geometry("400x400")

        # Lista interna de tareas (texto, estado)
        self.tareas = []

        # Entrada de texto
        self.entry = tk.Entry(root, width=30)
        self.entry.pack(pady=10)

        # Lista de tareas
        self.lista = tk.Listbox(root, width=40, height=10)
        self.lista.pack(pady=10)

        # Botones
        self.btn_agregar = tk.Button(root, text="Agregar Tarea", command=self.agregar_tarea)
        self.btn_agregar.pack(pady=5)

        self.btn_completar = tk.Button(root, text="Marcar como Completada", command=self.completar_tarea)
        self.btn_completar.pack(pady=5)

        self.btn_eliminar = tk.Button(root, text="Eliminar Tarea", command=self.eliminar_tarea)
        self.btn_eliminar.pack(pady=5)

        # 🔹 Atajos de teclado CORREGIDOS
        self.root.bind("<Return>", self.agregar_tarea)          # Enter
        self.root.bind("<Control-c>", self.completar_tarea)     # Ctrl + C
        self.root.bind("<Control-d>", self.eliminar_tarea)      # Ctrl + D
        self.root.bind("<Escape>", lambda e: self.root.quit())  # Escape

    # 🔹 Agregar tarea
    def agregar_tarea(self, event=None):
        texto = self.entry.get()
        if texto.strip() != "":
            self.tareas.append((texto, False))  # False = pendiente
            self.actualizar_lista()
            self.entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Aviso", "Escribe una tarea")

    # 🔹 Marcar como completada
    def completar_tarea(self, event=None):
        seleccion = self.lista.curselection()
        if seleccion:
            index = seleccion[0]
            texto, estado = self.tareas[index]
            self.tareas[index] = (texto, True)
            self.actualizar_lista()
        else:
            messagebox.showwarning("Aviso", "Selecciona una tarea")

    # 🔹 Eliminar tarea
    def eliminar_tarea(self, event=None):
        seleccion = self.lista.curselection()
        if seleccion:
            index = seleccion[0]
            del self.tareas[index]
            self.actualizar_lista()
        else:
            messagebox.showwarning("Aviso", "Selecciona una tarea")

    # 🔹 Actualizar lista visual
    def actualizar_lista(self):
        self.lista.delete(0, tk.END)
        for texto, estado in self.tareas:
            if estado:
                self.lista.insert(tk.END, f"✔ {texto}")
                self.lista.itemconfig(tk.END, fg="green")
            else:
                self.lista.insert(tk.END, f"✘ {texto}")
                self.lista.itemconfig(tk.END, fg="red")


# Ejecutar aplicación
if __name__ == "__main__":
    root = tk.Tk()
    app = AplicacionTareas(root)
    root.mainloop()