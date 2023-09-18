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
while True:
    numero=int(input('ingresa un numero: '))
    if numero == 5:
        print('correcto, ganaste el premio')
        break


