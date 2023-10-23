from tkinter import*

def eval():
    us=user.get()
    cr=int(contra.get())
    if cr ==12345678:
        mensaje=Label(ventana,text=f'''
        Hola usuario {us}, 
        la contraseña es correcta.
        .....................................
        Bienvenido 😁''') 
        mensaje.grid(row=3)
    else:
        mensaje=Label(ventana,text=f'''
        Hola usuario {us}
        la contraseña es incorrecta.
        .....................................
        lo sentimos🙂''') 
        mensaje.grid(row=3)

def limpiar():
    user.delete(0,END)
    contra.delete(0,END)
    user.focus()


           
ventana =Tk()
ventana.title('CORREO😄')
ventana.geometry("300x200")
ventana.config(bg='grey')

widget_dos=Frame()
widget_dos.grid(row='2',column='0')
widget_dos.config(height='30',width='30')
widget_dos.config(bg='grey') 

et=Label(ventana, text="USUARIO ")
et.grid(row=0,column=0)

etiqueta =Label(ventana, text="PASSWORD")
etiqueta.grid(row=1,column=0)

user=Entry(ventana)
user.config(bg='black',fg='white')
user.grid(row=0,column=1)

contra=Entry(ventana,show='*')
contra.config(bg='black',fg='white')
contra.grid(row=1,column=1)

boton=Button(ventana,text='Evaluar',command=eval)
boton.grid(row=3,column=0)
#boton.config(bg='pink')

boton_limpiar=Button(ventana,text='Limpiar',command=limpiar).grid(row=3,column=1) 
#boton_limpiar.config(bg='pink')

ventana.mainloop()



