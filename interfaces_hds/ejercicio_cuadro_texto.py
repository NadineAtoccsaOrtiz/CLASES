## creacion de etiquetas
from tkinter import *
ventana= Tk()
ventana.title('Bienvenid@')
ventana.geometry('400x500')

widget_uno=Frame()
widget_uno.grid(row='0', column='0')
widget_uno.config(height='100',width='500')
widget_uno.config(bg='pink')

widget_dos=Frame()
widget_dos.grid(row='3',column='0')
widget_dos.config(height='100',width='500')
widget_dos.config(bg='pink')


# primero instanciar la variable
etiqueta=Label(ventana, text='Ingresa tu nombre: ')
etiqueta.grid(row=1, column=0)

## cuadro de texto -- entry
cuadro_texto=Entry()
cuadro_texto.grid(row='2',column='0')  ## grid es para ubicar en filas o columnas 


ventana.mainloop()
