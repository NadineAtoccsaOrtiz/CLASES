## creacion de etiquetas
from tkinter import *
ventana= Tk()
ventana.title('Bienvenid@')
ventana.geometry('400x500')

widget_uno=Frame()
widget_uno.grid(row='0', column='0')
widget_uno.config(height='200',width='500')
widget_uno.config(bg='pink')

widget_dos=Frame()
widget_dos.grid(row='2',column='0')
widget_dos.config(height='200',width='500')
widget_dos.config(bg='pink')


# primero instanciar la variable
etiqueta=Label(ventana, text='hola soy una etiqueta sexy xd')
etiqueta.grid(row=1, column=0)

ventana.mainloop()
