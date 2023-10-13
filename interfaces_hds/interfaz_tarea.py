from tkinter import *

ventana= Tk() 

widget_uno=Frame()

widget_uno.grid(row='0',column='0')
widget_uno.config(width='100',heigth='100')
widget_uno.config(bg='blue')

widget_dos=Frame()
widget_dos.grid(row='2',column='0')
widget_dos.config(width="100",height="100")
widget_dos.config(bg='green')

ventana.mainloop()