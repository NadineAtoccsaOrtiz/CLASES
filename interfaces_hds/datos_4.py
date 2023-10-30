from tkinter import *
ventana= Tk()
ventana.title('Bienvenid@')
ventana.geometry('400x500')


widget_dos=Frame()
widget_dos.grid(row='0',column='0')
widget_dos.config(height='20',width='50')

widget_dos=Frame()
widget_dos.grid(row='1',column='0')
widget_dos.config(height='20',width='50')

widget_dos=Frame()
widget_dos.grid(row='2',column='0')
widget_dos.config(height='20',width='50')

widget_dos=Frame()
widget_dos.grid(row='3',column='3')
widget_dos.config(height='20',width='30')

#####
widget_dos=Frame()
widget_dos.grid(row='5',column='4')
widget_dos.config(height='20',width='30') 

widget_dos=Frame()
widget_dos.grid(row='6',column='1')
widget_dos.config(height='70',width='120')
widget_dos.config(bg='pink')

# primero instanciar la variable
etiqueta=Label(ventana, text='Nombres y Apellidos: ')
etiqueta.grid(row=0, column=0)

etiqueta=Label(ventana, text='DNI: ')
etiqueta.grid(row=2, column=0)

etiqueta=Label(ventana, text='Celular: ')
etiqueta.grid(row=4, column=0)


## cuadro de texto -- entry
cuadro_texto=Entry()
cuadro_texto.grid(row='0',column='1') 

cuadro_texto=Entry()
cuadro_texto.grid(row='2',column='1') 

cuadro_texto=Entry()
cuadro_texto.grid(row='4',column='1') 
########
ventana.mainloop()