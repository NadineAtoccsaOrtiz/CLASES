from tkinter import *
ventana=Tk()
ventana.title('CALCULADORA')

##clase operadores
class Operadores:
  def sumar(self,num1,num2):
    return num1+num2
  def restar(self,num1,num2):
    return num1-num2
  def dividir(self,num1,num2):
    return num1//num2
  def multiplicar(self,num1,num2):
    return num1*num2
  

##manejador de operadores
operacion=StringVar()
classOperadores=Operadores()
def manejadorOperaciones():
  num1=int(textoUno.get())
  num2=int(textoDos.get())
  ope=operacion.get()
  if ope=="+":
    resultado=classOperadores.sumar(num1,num2)
    Label(ventana,text=f"el resultado de la suma es: {resultado}").pack()
  elif ope=="-":
    resultado=classOperadores.restar(num1,num2)
    Label(ventana,text=f"el resultado de la resta es: {resultado}").pack()
  elif ope=="/":
    resultado=classOperadores.dividir(num1,num2)
    Label(ventana,text=f"el resultado de la Division es: {resultado}").pack()
  elif ope=="*":
    resultado=classOperadores.multiplicar(num1,num2)
    Label(ventana,text=f"el resultado de la Multiplicacion es: {resultado}").pack()

##primer cuadro
etiquetaNumUno=Label(ventana,text="ingrese el primer numero").pack()
textoUno=Entry(ventana)
textoUno.pack()

##segundo cuadro
etiquetaNumDos=Label(ventana,text="ingrese el segundo numero").pack()
textoDos=Entry(ventana)
textoDos.pack()

##cuadro del total
etiquetaResultado=Label(ventana,text="el resultado es el siguiente").pack()
textoResultado=Entry(ventana)
textoResultado.pack()

##opciones
opcionSuma=Radiobutton(ventana,text="+",value="+",variable=operacion).pack()
opcionResta=Radiobutton(ventana,text="-",value="-",variable=operacion).pack()
opcionDivision=Radiobutton(ventana,text="/",value="/",variable=operacion).pack()
opcionMultiplicacion=Radiobutton(ventana,text="*",value="*",variable=operacion).pack()

##botones
b1=Button(ventana,text='1',command==)

botonCalcular=Button(ventana,text="calcular",command=manejadorOperaciones)
botonCalcular.pack()

ventana.mainloop()