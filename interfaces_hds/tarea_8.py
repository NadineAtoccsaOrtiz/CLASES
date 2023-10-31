# from tkinter import *
# ventana=Tk()
# ventana.title('CALCULADORA BASICA')

# class Calculadora():

import tkinter as tk

class Calculadora:

    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("Calculadora")
        
        self.i = 0
        self.operacion = ""
        self.resultado = 0

        # Pantalla de operación
        self.mostrar_operacion = tk.StringVar()
        self.pantalla_operacion = tk.Entry(ventana, textvariable=self.mostrar_operacion)
        self.pantalla_operacion.grid(columnspan=4, ipadx=70)
        
        # Pantalla de resultado 
        self.mostrar_resultado = tk.StringVar() 
        self.pantalla_resultado = tk.Entry(ventana, textvariable=self.mostrar_resultado)
        self.pantalla_resultado.grid(columnspan=4, ipadx=70)
        
        # Botones de dígitos
        boton7 = tk.Button(ventana, text="7", command=lambda: self.agregar_digito(7))
        boton8 = tk.Button(ventana, text="8", command=lambda: self.agregar_digito(8))
        boton9 = tk.Button(ventana, text="9", command=lambda: self.agregar_digito(9))
        boton4 = tk.Button(ventana, text="4", command=lambda: self.agregar_digito(4))
        boton5 = tk.Button(ventana, text="5", command=lambda: self.agregar_digito(5))
        boton6 = tk.Button(ventana, text="6", command=lambda: self.agregar_digito(6))
        boton1 = tk.Button(ventana, text="1", command=lambda: self.agregar_digito(1))
        boton2 = tk.Button(ventana, text="2", command=lambda: self.agregar_digito(2))
        boton3 = tk.Button(ventana, text="3", command=lambda: self.agregar_digito(3))
        boton0 = tk.Button(ventana, text="0", command=lambda: self.agregar_digito(0))

        # Botones de operadores
        boton_suma = tk.Button(ventana, text="+", command=lambda: self.agregar_operador("+"))
        boton_resta = tk.Button(ventana, text="-", command=lambda: self.agregar_operador("-"))
        boton_multi = tk.Button(ventana, text="*", command=lambda: self.agregar_operador("*"))
        boton_div = tk.Button(ventana, text="/", command=lambda: self.agregar_operador("/"))        
        boton_igual = tk.Button(ventana, text="=", command=self.calcular)
        
        # Posicionar botones con grid
        boton7.grid(row=2, column=0) 
        # ... Posicionar todos los botones

    def agregar_digito(self, digito):
        self.operacion += str(digito)
        self.i += 1
        self.mostrar_operacion.set(self.operacion)
        
    def agregar_operador(self, operador):
        self.operacion += str(operador)
        self.i += 1
        self.mostrar_operacion.set(self.operacion)
        
    def calcular(self):
        try:
            self.resultado = str(eval(self.operacion))
            self.mostrar_resultado.set(self.resultado)
        except:
            self.mostrar_resultado.set("ERROR")
        finally:
            self.operacion = ""
            self.i = 0
        
ventana = tk.Tk()
app = Calculadora(ventana)
ventana.mainloop()