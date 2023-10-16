from tkinter import *

ventana= Tk() 

widget_uno=Frame()

widget_uno.grid(row='0', column='0')
widget_uno.config(height='100',width='100')
widget_uno.config(bg='blue')

widget_dos=Frame()
widget_dos.grid(row='0',column='1')
widget_dos.config(height='100',width='100')
widget_dos.config(bg='red')

widget_dos=Frame()
widget_dos.grid(row='1',column='0')
widget_dos.config(height='100',width='100')
widget_dos.config(bg='yellow')

widget_dos=Frame()
widget_dos.grid(row='1',column='1')
widget_dos.config(height='100',width='100')
widget_dos.config(bg='green')

widget_dos=Frame()
widget_dos.grid(row='2',column='0')
widget_dos.config(height='100',width='100')
widget_dos.config(bg='pink')

widget_dos=Frame()
widget_dos.grid(row='2',column='1')
widget_dos.config(height='100',width='100')
widget_dos.config(bg='purple')
#

ventana.mainloop()
