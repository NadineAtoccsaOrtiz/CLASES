from tkinter import *
from funciones import *

ventana=Tk()
ventana.title('CALCULADORA')
ventana.geometry('296x300')
ventana.resizable(0,0)
fuente=('arial',9,'bold')


# pantalla que muestra los numeros ingresados y el resultado
pantalla=Entry(ventana, 
                width=22, # width ancho y heigth es para la altura
                bg="brown", #color de fondo
                fg="white", # asigna el color al texto
                borderwidth=0, # tamaño del borde dl cuadro de texto, 0 significa sin borde 
                font=('arial',18,'bold')) # formato de letra 
pantalla.grid(row=0,columnspan=4,padx=4,pady=4)

# botones de la calculadora # boton numeros
boton1 = Button(ventana, text="1", height=3, width=9, bg='white',fg='red',borderwidth=0,cursor='hand2', font=fuente, command=lambda: enviar_dato(1,pantalla))
boton2 = Button(ventana, text="2", height=3, width=9, bg='white',fg='red',borderwidth=0,cursor='hand2', font=fuente, command=lambda: enviar_dato(2,pantalla))
boton3 = Button(ventana, text="3", height=3, width=9, bg='white',fg='red',borderwidth=0,cursor='hand2', font=fuente, command=lambda: enviar_dato(3,pantalla))
boton4 = Button(ventana, text="4", height=3, width=9, bg='white',fg='red',borderwidth=0,cursor='hand2', font=fuente, command=lambda: enviar_dato(4,pantalla))
boton5 = Button(ventana, text="5", height=3, width=9, bg='white',fg='red',borderwidth=0,cursor='hand2', font=fuente, command=lambda: enviar_dato(5,pantalla))
boton6 = Button(ventana, text="6", height=3, width=9, bg='white',fg='red',borderwidth=0,cursor='hand2', font=fuente, command=lambda: enviar_dato(6,pantalla))
boton7 = Button(ventana, text="7", height=3, width=9, bg='white',fg='red',borderwidth=0,cursor='hand2', font=fuente, command=lambda: enviar_dato(7,pantalla))
boton8 = Button(ventana, text="8", height=3, width=9, bg='white',fg='red',borderwidth=0,cursor='hand2', font=fuente, command=lambda: enviar_dato(8,pantalla)) 
boton9 = Button(ventana, text="9", height=3, width=9, bg='white',fg='red',borderwidth=0,cursor='hand2', font=fuente, command=lambda: enviar_dato(9,pantalla))
boton0 = Button(ventana, text="0", height=3, width=9, bg='white',fg='red',borderwidth=0,cursor='hand2', font=fuente, command=lambda: enviar_dato(0,pantalla))
botonpunto = Button(ventana, text=".", height=3, width=9, bg='white',fg='red',borderwidth=0,cursor='hand2', font=fuente, command=lambda: enviar_dato('.',pantalla))
# cursor -> sirve para cambiar el estilo del mouse cuando me pongo encima del boton 

# mostrar numeros
boton1.grid(row=1, column=0)
boton2.grid(row=1, column=1)  
boton3.grid(row=1, column=2)
boton4.grid(row=2, column=0)
boton5.grid(row=2, column=1)
boton6.grid(row=2, column=2)
boton7.grid(row=3, column=0)  
boton8.grid(row=3, column=1)
boton9.grid(row=3, column=2)
boton0.grid(row=4, column=0)
botonpunto.grid(row=4, column=2)
# boton suma
boton_suma = Button(ventana, text="+",height=3, width=9, bg='white',fg='red',borderwidth=0,cursor='hand2', font=fuente, command=lambda: operacion('+',pantalla))
boton_suma.grid(row=1, column=3)

# boton resta
boton_resta = Button(ventana, text="-",height=3, width=9, bg='white',fg='red',borderwidth=0,cursor='hand2', font=fuente, command=lambda: operacion('-',pantalla))#, command=lambda: click_boton("-"))
boton_resta.grid(row=2, column=3)

# boton multiplicacion
boton_mult = Button(ventana, text="*",height=3, width=9, bg='white',fg='red',borderwidth=0,cursor='hand2', font=fuente, command=lambda: operacion('*',pantalla))#, command=lambda: click_boton("*"))
boton_mult.grid(row=3, column=3)

# boton division
boton_div = Button(ventana, text="/",height=3, width=9, bg='white',fg='red',borderwidth=0,cursor='hand2', font=fuente, command=lambda: operacion('/',pantalla))#, command=lambda: click_boton("/"))
boton_div.grid(row=4, column=3)

# boton igual
boton_igual = Button(ventana, text="=", height=3, width=9, bg='white',fg='red',borderwidth=0,cursor='hand2', font=fuente, command=lambda: igual(pantalla))# , command=manejadorOperaciones)
boton_igual.grid(row=4, column=1)

# boton borrar
# boton_borrar = Button(ventana, text="Borrar",height=3, width=9, bg='white',fg='red',borderwidth=0,cursor='hand2', font=fuente, command=lambda:borrar(pantalla))
# boton_borrar.grid(row=4, column=2) 

# boton clear
boton_clear=Button(ventana, text="CLEAR",height=3, width=9, bg='white',fg='red',borderwidth=0,cursor='hand2', font=fuente, command=lambda:clear(pantalla))#, command=lambda: click_boton("/"))
boton_clear.grid(row=5,column=0,columnspan=4)



ventana.mainloop()