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
## label es una clase, primer parametro, damos el lugar donde se va crear la etiqueta,
# y el segundo va el texto que quiero mostrar
# label sirve para mostrar texto

ventana.mainloop()

## pack empaqueta apila, agrega 
etiqueta.pack()
## grid recibe dos parametros, fila y columna
