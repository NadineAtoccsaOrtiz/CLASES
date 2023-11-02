from tkinter import *

ventana = Tk()
ventana.title("Calculadora")

entrada = Entry(ventana)
entrada.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

class Operadores:
  def sumar(self,num1,num2):
    return num1+num2
  def restar(self,num1,num2):
    return num1-num2
  def dividir(self,num1,num2):
    return num1//num2
  def multiplicar(self,num1,num2):
    return num1*num2

def click_boton(numero):
    actual = entrada.get()
    entrada.delete(0, END)
    entrada.insert(0, actual + str(numero))
    
    
classOperadores=Operadores()
def manejadorOperaciones():
    num1=int(entrada.get())
    entrada.delete(0, END)
    operacion=StringVar(entrada.get())
    entrada.delete(0, END)
    num2=int(entrada.get())
    entrada.delete(0, END)
    ope=operacion.get()
    if ope=="+":
        resultado=classOperadores.sumar(num1,num2)

    elif ope=="-":
        resultado=classOperadores.restar(num1,num2)

    elif ope=="/":
        resultado=classOperadores.dividir(num1,num2)

    elif ope=="*":
        resultado=classOperadores.multiplicar(num1,num2)



def borrar():
    entrada.delete(0, END)
    

boton1 = Button(ventana, text="1", command=lambda: click_boton(1))
boton2 = Button(ventana, text="2", command=lambda: click_boton(2))
boton3 = Button(ventana, text="3", command=lambda: click_boton(3))
boton4 = Button(ventana, text="4", command=lambda: click_boton(4))
boton5 = Button(ventana, text="5", command=lambda: click_boton(5))
boton6 = Button(ventana, text="6", command=lambda: click_boton(6))
boton7 = Button(ventana, text="7", command=lambda: click_boton(7))
boton8 = Button(ventana, text="8", command=lambda: click_boton(8))
boton9 = Button(ventana, text="9", command=lambda: click_boton(9))
boton0 = Button(ventana, text="0", command=lambda: click_boton(0))

boton_suma = Button(ventana, text="+", command=click_boton)
boton_resta = Button(ventana, text="-", command=click_boton)
boton_multiplicacion = Button(ventana, text="*", command=click_boton)
boton_division = Button(ventana, text="/", command=click_boton)
boton_igual = Button(ventana, text="=", command=manejadorOperaciones)
boton_borrar = Button(ventana, text="Borrar", command=borrar)

boton1.grid(row=1, column=0)
boton2.grid(row=1, column=1)  
boton3.grid(row=1, column=2)

boton4.grid(row=2, column=0)
boton5.grid(row=2, column=1)
boton6.grid(row=2, column=2)

boton7.grid(row=3, column=0)  
boton8.grid(row=3, column=1)
boton9.grid(row=3, column=2)

boton0.grid(row=4, column=0)
boton_borrar.grid(row=4, column=2)  
boton_suma.grid(row=1, column=3)
boton_resta.grid(row=2, column=3)
boton_multiplicacion.grid(row=3, column=3)
boton_division.grid(row=4, column=3)
boton_igual.grid(row=4, column=1)

ventana.mainloop()