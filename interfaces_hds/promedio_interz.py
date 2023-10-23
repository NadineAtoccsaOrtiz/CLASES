from tkinter import*
ventana=Tk()

def promedio():
    dato=notas.get.split(",")
    suma=0
    for n in dato:
        suma=suma+int(n)
    promedio=suma//len(dato)
    notasr.insert(0,promedio)


def limpiar():
    notas.delete(0,END)
    notasr.delete(0,END)
    notas.focus()
    
et=Label(ventana,text='ingresa tus notas').grid(row=0,column=0)
notas=Entry(ventana)
notas.grid(row=0,column=1)


eti=Label(ventana,text='promedio').grid(row=1,column=0)
notasr=Entry(ventana)
notasr.grid(row=1,column=1)

boton=Button(ventana,text='calcular',command=promedio).grid(row=2,column=0)
boton_limpiar=Button(ventana,text='Limpiar',command=limpiar).grid(row=2,column=1)


ventana.mainloop()