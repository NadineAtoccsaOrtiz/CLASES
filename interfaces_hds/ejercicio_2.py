from tkinter import *

ventana= Tk() 

widget_uno=Frame()
widget_uno.grid(row='0',rowspan='2',column='0')
widget_uno.config(height='200',width='100')
widget_uno.config(bg='blue')

widget_dos=Frame()
widget_dos.grid(row='0',column='1')
widget_dos.config(height='100',width='100')
widget_dos.config(bg='red')

widget_tres=Frame()
widget_tres.grid(row='1',column='1')
widget_tres.config(height='100',width='100')
widget_tres.config(bg='yellow')

widget_cuatro=Frame()
widget_cuatro.grid(row='2',column='0',columnspan='2')
widget_cuatro.config(height='100',width='200')
widget_cuatro.config(bg='purple')

ventana.mainloop()