# importamos tkinter, tk es una clase
from tkinter import *

# instanciar 

ventana=Tk() # widget superior el cuadro completo

# creamos dos widget de orden inferior con la clase frame()

# instancio mi primer widget
widget_uno=Frame()
# usar metodod para montar frame
widget_uno.grid(row='0',column='0')
widget_uno.config(width='100',heigth='100')
widget_uno.config(bg='blue')
# el metodo grid recibe dos parametros, el numero de la columna  y el numero de la fila donde quiero ubicar mi widget

# segundo widget
widget_dos=Frame()
widget_dos.grid(row='2',column='0')
widget_dos.config(width='100',heigth='100')
widget_dos.config(bg='green')



# usar el metodo, es la funcionalidad, mainloop para que se mantenga abierta

ventana.mainloop()

