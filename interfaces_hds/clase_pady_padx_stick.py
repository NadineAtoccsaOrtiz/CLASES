from tkinter import *
ventana=Tk()
ventana.geometry('300x300')

frameL=LabelFrame(ventana,text='cuadrito',padx=20,pady=20)
frameL.config(height=200,width=200)
frameL.pack()
# pady=horisontal
# padx=vertical

variable=' 1'
texto=Entry(frameL)
texto.insert(0, variable+ 'mundo')
texto.pack()


ventana.mainloop()
