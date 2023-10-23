from tkinter import*

# Función para manejar el evento del botón
def boton_presionado():
    etiqueta.config(text="eqtiqueta ")
    pass
# Crear una ventana
ventana =Tk()
## dar titulo a la ventana
ventana.title('ventana suma')

# Definir el tamaño de la ventana
ventana.geometry("400x300")

# Crear un botón
boton =Button(ventana, text="Presionar", command=boton_presionado)
boton.pack()

# Crear una etiqueta
etiqueta =Label(ventana, text="clic")
etiqueta.pack()
## craer cuadro de texto, primero asociamos con la interzas de nombre ventana
text_nombre=Entry(ventana)
text_nombre.config(bg='black',fg='white')
text_nombre.pack()

# Ejecutar el bucle principal de la ventana, evita que la ventana se cierre
ventana.mainloop()



