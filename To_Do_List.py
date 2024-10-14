import tkinter as tk
from tkinter import font


# Create principal window
app = tk.Tk()
app.geometry("600x300")
app.configure(background="black")
tk.Wm.wm_title(app, "To Do List")



# Create label to show content
label_font = font.Font(size=14)  # Definir un tamaño de fuente mayor
label = tk.Label(app, text="", justify="left", bg="black", fg="white", font=label_font, anchor="nw")
label.pack(fill="both", expand=True, padx=10, pady=10)  # Alinear a la izquierda y agregar espacio alrededor



# Create a frame to save buttons
button_frame = tk.Frame(app)
button_frame.pack(pady=10)  # Espacio alrededor del frame de botones


# Creat a Entry to save the input of tasks
task_entry = tk.Entry(app, width=50)  # Tamaño del Entry
task_entry.pack(pady=10)  # Espacio alrededor del Entry



def add_task():
    tarea = task_entry.get()  # Obtener texto del Entry
    if tarea:  # Comprobar si hay texto en el Entry
        with open("Interfaces/To_Do_List/text_file.txt", "a") as my_task:
            my_task.write(tarea + "\n")
        task_entry.delete(0, tk.END)  # Limpiar el Entry
        refresh_label()  # Actualiza el Label después de añadir la tarea


def delete_task():
    tarea = task_entry.get()  # Obtener texto del Entry
    if tarea:  # Comprobar si hay texto en el Entry
        with open("Interfaces/To_Do_List/text_file.txt", "r") as open_file:
            lines = open_file.readlines()

        with open("Interfaces/To_Do_List/text_file.txt", "w") as my_task:
            for line in lines:
                if line.strip() != tarea:  # Eliminar la línea que coincide
                    my_task.write(line)

        task_entry.delete(0, tk.END)  # Limpiar el Entry
        refresh_label()  # Actualiza el Label después de eliminar la tarea
    else:
        print("Por favor, introduce una tarea para eliminar.")


def refresh_label():
    try:
        with open("Interfaces/To_Do_List/text_file.txt", "r") as archivo:
            contenido = archivo.read()
        label.config(text=contenido)  # Actualizar el texto del Label
    except FileNotFoundError:
        label.config(text="El archivo no existe.")



tk.Button(                                  
    button_frame,
    text="Add Task",
    bg="green",
    fg="black",
    command=add_task,
    font=("Courier", 14)
).pack(side="left", padx=1)

tk.Button(
    button_frame,
    text="Delete Task",
    bg="red",
    fg="black",
    command=delete_task,
    font=("Courier", 14)
).pack(side="left", padx=1)

refresh_label()

tk.mainloop()