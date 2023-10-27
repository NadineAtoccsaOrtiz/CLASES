from tkinter import*

def eval():
    ed=int(edad.get())
    txt=(nombre.get())
    if ed <=18:
        mensaje=Label(ventana,text=f'''Hola {txt}, Tienes {ed}  y eres menor de edad''') 
        mensaje.grid(row=3)
    else:
        #if edd >=18:
        mensaje=Label(ventana,text=f'''Hola {txt}, Tienes {ed}  y eres mayor de edad''') 
        mensaje.grid(row=3)

    #mensaje=Label(ventana,text=f'''Hola {txt}, Tienes {ed}  y eres ''') 
        
ventana =Tk()
ventana.title('Evalua tu Edad😄')
ventana.geometry("400x300")

et=Label(ventana, text="ingresa tu nombre")
et.grid(row=0,column=0)

etiqueta =Label(ventana, text="ingresa tu edad")
etiqueta.grid(row=1,column=0)

nombre=Entry(ventana)
nombre.config(bg='black',fg='white')
nombre.grid(row=0,column=1)

edad=Entry(ventana)
edad.config(bg='black',fg='white')
edad.grid(row=1,column=1)

boton=Button(ventana,text='Evaluar',command=eval)
boton.grid(row=2,column=0)

ventana.mainloop()



