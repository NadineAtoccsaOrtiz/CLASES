from tkinter import *
from funciones import enviar_dato 
ventana = Tk()
ventana.title("Calculadora")

class Operadores:
  def sumar(self,num1,num2):
    return num1+num2

  def restar(self,num1,num2):
    return num1-num2

  def dividir(self,num1,num2):
    return num1//num2

  def multiplicar(self,num1,num2):
    return num1*num2

entrada = Entry(ventana)
entrada.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

def click_boton(numero):
  actual = entrada.get()
  entrada.delete(0, END)
  entrada.insert(0, actual + str(numero))

classOperadores = Operadores()

def manejadorOperaciones():
  num1 = int(entrada.get()) #.split('+')or('-')or('*')or('/')
  entrada.delete(0, END)

  operacion = entrada.get()
  entrada.delete(0, END)

  num2 = int(entrada.get())
  entrada.delete(0, END)



  if operacion == "+":
    resultado = classOperadores.sumar(num1,num2)
  elif operacion == "-":
    resultado = classOperadores.restar(num1,num2)
  elif operacion == "/":
    resultado = classOperadores.dividir(num1,num2)
  elif operacion == "*":
    resultado = classOperadores.multiplicar(num1,num2)

  entrada.insert(0, resultado)

def borrar():
  entrada.delete(0, END)

# Botones número 
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

# Ubicación botones
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


boton_igual = Button(ventana, text="=", command=manejadorOperaciones)
boton_borrar = Button(ventana, text="Borrar", command=borrar)
boton_suma = Button(ventana, text="+", command=lambda: click_boton("+"))
boton_resta = Button(ventana, text="-", command=lambda: click_boton("-"))
boton_mult = Button(ventana, text="*", command=lambda: click_boton("*"))
boton_div = Button(ventana, text="/", command=lambda: click_boton("/"))


boton_borrar.grid(row=4, column=2)  
boton_suma.grid(row=1, column=3)
boton_resta.grid(row=2, column=3)
boton_mult.grid(row=3, column=3)
boton_div.grid(row=4, column=3)
boton_igual.grid(row=4, column=1)
#...
# Ubicación botones
boton_borrar.grid(row=4, column=2)  
boton_suma.grid(row=1, column=3)
#...

ventana.mainloop()
