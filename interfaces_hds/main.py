
import tkinter as tk

# Función para manejar el evento del botón
def boton_presionado():
    etiqueta.config(text="hola, bienvenid@")

# Crear una ventana
ventana = tk.Tk()

# Definir el tamaño de la ventana
ventana.geometry("400x300")

# Crear un botón
boton = tk.Button(ventana, text="Presionar", command=boton_presionado)
boton.pack()

# Crear una etiqueta
etiqueta = tk.Label(ventana, text="Presiona el botón")
etiqueta.pack()

# Ejecutar el bucle principal de la ventana
ventana.mainloop()



