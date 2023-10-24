from tkinter import*
ventana=Tk()
ventana.title('mi ventana')
ventana.geometry('500x400')

colum_izquierda=Frame()
colum_izquierda.grid(row=0,column=0)
colum_izquierda.config(height=5,width=200)


etiqueta=Label(ventana,text='esta es mi etiqueta')
etiqueta.grid(row=0,column=1)

# header=Frame().grid(row=0,column=0) ## avreviar para menos lineas de codigo pero no en python
header=Frame()
header.grid(row=0,column=0)
header.config(height=10 ,width=500,bg='red')

aside_right=Frame()
aside_right.grid(row=1,column=0)
aside_right.config(height=385 ,width=15,bg='red')


etiqueta_usuario=Label(ventana,text='Usuario').grid(row=1,column=1)
text_usuario=Entry(ventana).grid(row=1,column=2)

section_uno=Frame()
section_uno.grid(row=2,column=1)
section_uno.config(height=2,width=0,bg='red')

etiqueta_password=Label(ventana,text='Password').grid(row=3,column=1)
text_password=Entry(ventana,show='').grid(row=3,column=2) ## dentro de entry hay una propiedfad llamada show, para reemplazar el texto en asterisqcos, para que nos e vea lo que escribo


ventana.mainloop()
