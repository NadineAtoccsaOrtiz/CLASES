# 1. importar tkinter -> libreria para la creacion de interfaz grafica
# import tkinter as tk
# root=tk.tk()

#otra manera de llamar a tkinter
from tkinter import *

# la libreria tkinter tiene 3 grandes clases para la creacion de interfcaes graficas, 
# las mas usada es tk()
# existe otra que es el tkk()
# la otra es tcl()

# 2.- instanciar tk() como generador de interfaz grafica 
#como instanciamos la clase, con una variable

nueva_ventana=tk.tk()

# otra herramienta, la parte basica de tk(), es el frame

# 3.  frame es tambien una clase = debe tener la primera letra con mayuscula 
# tiene atributos, funcionalidades
# para crear un frame primero tengo que instanciar , crear una variable donde se  almacene una clase
menu_principal=frame()
menu_principal.pack() # para empaquetar metodo para que funcione la configuracion, montamos o inicializamos el frame
# haciendo uso del metodod config loe asiganmos tamaño y color 

# intsanciamos nuestrta clase
menu_principal.config(width='200', height='200')
# le damos un tamaño, ancho de 200 y largo de 200, creamos un cuadrado
# le damos un color con bg = bag graw
menu_principal.config(bg ='red')

# mainloop es un metodo de tk() que mantiene la ejecucion del programa en un bucle 
nueva_ventana.mainloop()


## otro metodo similar a pack, para poner dos colores de fondo


