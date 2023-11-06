from tkinter import *

def enviar_dato(valor,pantalla):
    anterior=pantalla.get()
    pantalla.delete(0, END)
    pantalla.insert(0,str(anterior)+str(valor))

def operacion(signo,pantalla):
    global num1
    global signo_ope
    num1=pantalla.get()
    num1=float(num1)
    pantalla.delete(0,END)
    signo_ope=signo
    
# def suma(pantalla):
#     resultado=num1+num2
#     return resultado

# def resta(pantalla):
#     resultado=num1-num2
#     return resultado

# def multiplicar(pantalla):
#     resultado=num1*num2
#     return resultado

# def dividir(pantalla):
#     resultado=num1/num2
#     return resultado 

def igual(pantalla):
    global num2
    num2=pantalla.get()
    num2=float(num2)
    pantalla.delete(0,END)
    match signo_ope:
        case '+':
            pantalla.insert(0,num1+num2)
        case '-':
            pantalla.insert(0,num1-num2)
        case '*':
            pantalla.insert(0,num1*num2)
        case '/':
            pantalla.insert(0,num1/num2)

def borrar(pantalla):
    pantalla.delete(1.0,END)
    
def clear(pantalla):
    pantalla.delete(0,END)
    

    
    

    
