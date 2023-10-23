from tkinter import*

# Función para manejar el evento del botón
def boton_presionado():
    etiqueta.config(text="etiqueta ")
    pass
def captura_d():
    txt=text_nombre.get()
    ##print(txt)
    mensaje=Label(ventana,text=f'''hola {txt}''') ## para que el mensaje salga en mi ventana y no en el terminal o consola
    mensaje.pack() ## todos los metodos tiene el nombre y seguido un parentesis
## dentro de la variable txt capturo lo que la persona va escribir en el cuadro de texto


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
### metodos de entry,  (insert, focus, delete, get)
# Ejecutar el bucle principal de la ventana, evita que la ventana se cierre

## crear boton
boton=Button(ventana,text='enviar',command=captura_d)
## en command la funcion que va ejecutar esa funcion
boton.pack()
ventana.mainloop()



