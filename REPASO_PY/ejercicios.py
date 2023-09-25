## 1. crear un programa que me pida la edad de una persona, si la edad es mayor o igual a 18, que me muestre un mensaje que diga  'eres mayor de edad' caso contrario que me muetsre un mensaje que diga 'eres menor de edad'
#edad= int(input('ingresa tu edad'))
#if edad >=18:
#    print('eres mayor de edad')
#else:
#    print('eres m,enor de edad')


## 2. Una tienda comercial desea hacer un descuento del 20%, crear un programa que me determine si el cliente se hace acrededor del descuento t6eniendo en cuenta lo siguiente, si el cliente realiza una compra de igual o mayor a 1000 soles, mostrar un mensaje que d8iga 'ganaste el descuento' en caso de que la compra no supere los 1000 soles entonces mostrar un mensaje que diga 'no aplicas al descuento de la compra <mostrar el monto de su compra>.

#print('Elige un producto deseado: ')
#print(f"""
#1 CAMISA------------------------100
#2 ZAPATOS-----------------------800
#3 PANTALON----------------------600
#4 SUETER------------------------300
#5 CHAQUETA----------------------500
#""")
#producto=int(input('introduzca el codigo del producto: '))
#precio = int(input("Introduzca el precio del producto: "))
#cantidad = int(input("Introduzca la cantidad de articulos: "))

#total_compra= precio*cantidad
#descuento=(total_compra * 20)/100
#descuento_total=total_compra - descuento
#if total_compra >= 1000:
#    print(f' eres acrededor del descuento de 20%, y el total de tu compra es {descuento_total}.🎁')
#else:
#    print(f'no eres acrededor del descuento del 20%, total de tu compra a pagar es {total_compra}.☹')

## 3. crear un programa que me pida 5 veces un nombre y por cada vez que lo pida muestre la cantidad de veces que ingreso el nombre

#for n in range (1,6):
#    nombre=input('ingresa tu nombre: ')
#    print(f'ingresaste {n} veces el nombre')


## 4. crear un programa que me pida un numero y lo evalue con el numero premiado el programa finalizara, si el numero igresado es incorrecto el programa seguira pidiendo el numero premiado
#while True:
#    numero=int(input('ingresa un numero: '))
#    if numero == 5:
#        print('correcto, ganaste el premio')
#        break
## otra forma
#numero_ganador=50
#condicion=True
#while condicion:
#    numero_ingresado=int(input('ingresa un numero: '))
#    if numero_ingresado == numero_ganador:
#        print('ganaste hvnz')
#        condicion=False
#    else:
#        print('sigue intentando')
        

## 5. crear una funcion por cada operador arimetico que reciba dos parametros y retorne el resultado de la operacion
## ojo, crearse una funcion quq nos permita imprimir el resultado

#op=(input('ingresa la operacion que quieres realizar'))
def mostrar(texto):
    prin(texto)

def sumar(resultado):
    suma =num1+num2
    print("el resultado de la suma es: ", suma)
    
def restar(resultado):
    resta =num1-num2
    print("el resultado de la resta es: ", resta)

def multiplicar(self):
    multiplicacion =num1*num2
    print("el resultado de la multiplicación es: ", multiplicacion)

def dividir(self):
    divicion =num1/num2
    print("el resultado de la divición es: ", divicion)

#op=(input('ingresa la operacion que quieres realizar'))

#num1 = 12
#num2 = 11


## otra forma
#def mi_print(texto):
#    print(texto)
#def suma(a,b):
#    return a+b
#def resta(a,b):
#    return a-b
#def multiplicacion(a,b):
#    return a*b
#def division(a,b):
#    return a/b

#mi_print(suma(a,b))
#mi_print(resta(a,b))
#mi_print(multiplicacion(a,b))
#mi_print(dividir(a,b))


## 6. Escribe una funcion que reciba un numero entero 
# positivo y devuelva su factorial

num = int(input('ingresa un numero positivo: '))

def factorial(n):
    if n == 0:
        return 1
    if num < 0: 
        print("error, ingresaste un numero negativo")
    else:
        return n * factorial(n - 1)
result = factorial(num)
print(result)

## 7. escribir una funcion que reciba como parametros una lista 
# de numeros y retorne una nueva lista con el cuadro de cada numero 
# de la lista ingresada
lista_numeros=[2,4,8]
def funcion(lista):
    nueva_lista=[]
    for numero in lista:
        nueva_lista.append(numero**2)
    return nueva_lista
#print(funcion(45,50,15,20))

print(funcion(lista_numeros))


## 8. escribir un programa que reciba una cadena de caracteres y
# devuelva un objeto con cada palabra que contiene y su frecuencia

## 8. Escribir un programa que reciba una cadena de caracteres y 
# debuelva un objeto con cada palabra que contiene y su frecuencia
def frec_palabras(cadena):
    frecuencia_palabras = {}
    palabras = cadena.split()

    for palabra in palabras:
        if palabra in frecuencia_palabras:
            frecuencia_palabras[palabra] += 1
        else:
            frecuencia_palabras[palabra] = 1

    return frecuencia_palabras

cadena =input('Ingresa un texto: ')
resultado = frec_palabras(cadena)
print(resultado)
