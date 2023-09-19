# REPASO PYTHON
## 1. TIPOS DE DATOS
TIPOS DE DATOS PRIMITIVOS
+ string 
    - 'a' --> string o cadena de texto
    - 'hola' --> esto tambien es un string
    - 'hola soy un string y te saludo' --> cadena larga
    - '100' --> es un string 
    - 'false' 
    - "hola" 
    - "  " el espacio trambien es un string 
> NOTA:
> todo lo que este en comillas es un string
> no importa el contenido, mientras esteb en comillas es un tipo de dato string
> un string puede estar entre comillas simples o doble

+ numericos 
    - 100 => este es un tipo de dato numerico, y es un tipo de dato entero, en ingles integer
    - 2.1 => esate es un tipo de dato numerico flotante, en ingles float
+ booleano
    - false => tipo de dato booleano pero es de tipo falso
    - true => tipo de dato booleano de tipo verdadero

## 2. VARIABLES
Cuando queremos almacenar un tipo de dato, usamos las variables.
se llama variable, por que al almacenar los datos, estos pueden mutar, cambiar o modifcarse.
La variable es la misma pero los datos contenidos dentro de ella son los que van acambiar.

¿como creamos una variable para almacenar nuestros datos?

1. darle un nombre significativo o relacionado al dato que estamos guardando o almacenando 
2. indicarle a que dato esta asociado o relacionado, (a este paso se le conoce como asignacion)
3. indicar el tipo de dato que se va almacenar --> darle el dato  a guardar 
    
    nombre variable => asignacion => dato 

``Ejemplos:``

primero pedimos el dato a la personas, la edad de nadine:
```python
edad_nadine = 18
```
el nombre de un alumno 
```python
nombre_alumno= 'edwin'
```


## 3. OPERADORES
Las variables tambien almacenan operaciones
los operadores arimeticos: son 4
- suma (+)
    ```python
    suma=45+12
    ```
- resta (-)
    ```python
    resta=45-12
    ```
- multiplicacion (*)
    ```python
    multiplicacion=4*5
    ```
- division (/)
    ```python
    division=45/12
    ```
la variable va almacenar el resultado de la operacion arimetica.

``Ejemplo de operacion:``
```python
operacion=(45+12+23)/4
op=15+12+14+13/4
```
precedencia de operadores 

hay operadores de uso especial 
- suma normal 
```python
suma = 45+12 
```
da como resultado 87
- concatenar 
```python
concatenar = '45'+12
```
da como resultado 4212

- suma de palabras 
```python
suma ='hola'+'mundo'
```
el resultado es holamundo
- suma de palabras mas espacio
```python
salud2 = 'hola'+' '+'mundo'
```
el resultado es hola mundo
- suma y multiplicacion de palabras
```python
saludos = 'hola '+'mundo' * 3 
```
el resultado es , mundomundomundohola

## 4. DATOS ESTRUCTURADOS
datos que ya tienen una estrutura, exiten dos tipos
+ las listas
 
    se pueden almacenar distintos tipos de datos en una sola lista
    ```python
        lista=['nombre',10,false]
        lista_amigos=['jory','edwin','adan','chinita']
    ```
    
+ los objetos

Tambien al igual que las listas, almacenan distintos tipos de datos pero con un orden, para almacenar datos en un objeto necesitamos especificar un indice y un valor, a esto se le conoce como
indice => valor
```python
    {
        'nombre':'jory',
        'edad':52,
        'sexo':'todos los dias'
    }
```
se puede combinar ambas estructuras, las listas y objetos, como tambien pueden haber objetos dentro de un objeto,etc.

```python
    {
        'nombre':'jory',
        'edad':30,
        'amigos':['anthony','edwin','china']
        'direccion':{
            'departamento':'ayacucho',
            'provincia':'lucanas',
            'distrito':'puquio',
            'jiron':'san peter',
            'numero':152
        }

    }
alumnos=[{},{},{}]

```

## 5. controles de flujo
Existen solo 2:
+ desiciones

solo se va ejecutar el codigo si cumple o si la condicion es verdadera, podemos hacer que si la condicion sea falsa se ejecute otro codigo

``Ejemplo de sintaxis``

Primero especificar el codigo que se ejcutara si cumple una condicion 
```python
if  <condicion>:
```
El codigo que deseamos ejecutar, si la condicion es verdadera  
 ```python
    print("ejecuta esto")
 ```
Aqui estamos fuera del if o del (si), este codigo siempre se ejecutara, por que estan en la misma altura , es decir depende de la identacion 
```python
print("esto siempre se ejecuta")
```

``Ejemplo de sintaxis mas complejo``

si queremos que se ejecute un codigo en caso sea falso, para eso tenemos la condicion else.
```python
if <condicion falsa>:
    print('si es verdadero ejecuta esto')
else:
    print('si es falso ejecuta esto')

```
>NOTA:
    - mayor --> (>)
    - menor --> (<)
  
``Ejemplo``

```python
if 15>18
    print('si es verdad imprime esto')
else:
    print('si es falso imprime esto')
```
``Otro ejemplo``
```python
if 15*12==30:
    print('si es verdad imprime esto')
else:
    print('si es falso imprime esto')
```
``Ejemplo mas complejo``
```python
condicion=True
if condicion:
    print('si es verdad imprime esto')
else:
    print('si es falso imprime esto')
```

+ ciclos

    Existen 2 tipos:
  - iterar cuando sabemos la cantidad de veces que se va repetir  
  para este caso existe el for 
  
    ``sintaxis`` 

    Despues de la palabra reservada bfor dberemos crear una variable que almacene el numero que iremos iterando, es decir repitiendo.
    Luego tendremos que indicar el rango a iterra o losm elementos a iterar.


    ```python
    for i in range(1,5):
        print(i)
    ```
    ```python
    vocales=['a','e','i','8','u']
    for i in vocales:
        print(i)
    ```
    ```python
    numeros=[45,12,75,10,56]
    for i in numeros:
        print(i)
    ```
  - iterar cuando no sabemos la cantidad de veces que se va repetir, para eso usamos while
  todas las condiciones que son verdaderas (true) van a permitir que el codigo se ejecute, evalua si la condicion es verdadera al igual que for. si es falso (false) no ejecuta

    ```python
    condicion=True
    while condicion:
        print('hola')
        texto=input('ingresa tu nombre o salir para terminar el programa: ')
        if texto=='salir':
            condicion=False
    ```

## 6. FUNCIONES
Las funciones son miniprogramas, tambien se les conoce como modulos o fragmentos de codigo de uso exclusivo y especifico.

Existen 2 tipos de funciones:

1. Propias del lenguaje

    Ya vienen creadas e insertadas en el lenguaje en  python y estan listas para ser usadas. 
``Estructura de uso de una funcion``
    - tiene el nombre seguido de un parentecis.
        ```python
        funcion()
        ```
    - dentro del parentesis podremos pasarle datos que necsita la funcion para ejecutarse. 
    
    - Esta es un afuncion que sirve para mostrtar datos por medio de la consola.
        ```pyhton
        print('hola')
        len('dato')
        ```
    - Esta funcion nos permite saber la longitud de una lista o un string. Len nos devuelve un numero
        ```pyhton
        len('dato')
        print(len([1,2,3,4,5]))
        ```
    - Esta es una funcion que se detiene a esperar que el usuario introduzca informacion (input). Entre parentesis podremos escribir un mensaje que indique que accion realizara el usuario.
        ```python
        input('ingresa un dato')
        ```
    - Esta es una funcion que nos muestra el numero mayor de una lista.(max)
        ```python
        lista=[45,12,45,11,78,62]
        numero_mayor=max(lista)
        print(numero_mayor)
        ```
    - esta funcion nos muestra el numero menor de una lista. (min)
        ```python
        lista=[45,12,45,11,78,62]
        numero_menor=min(lista)
            print(numero_menor)
        ```
    - Opcion para vonvertir de un string a un numero entero. (string a int) 
  
        ``` python
        numero_string='100'
        numero_entero=int(numero_string)
        print(numero_entero)
        


        ```
        int('100') --> 100 --> entero
    - opcion para convertir un entero a string. 
        ```python
        numero_entero=100
        numero_entero=str(numero_string)
        print(numero_string)
        ```
        str(100) --> '100' --> string
    - Funcion de python que nos permite agregar elemntos al final de una lista.(append)
        ```python
        lista=[15,12,50]
        elemento=100
        lista.append(elemento)
        print(lista)
        ```
    - funcion de python que nos permite eliminar los elementos que se encuentran al final de un alista.(pop)
        ```python
        lista=[15,12,50]
        lista.pop()
        print(lista)
        ```
    - funcion de python que nos permite agregar elementos en cuaqluier posicion de mi lista para eso se le tiene que pasar dos parametros, primero indicarle el indice y el dato que se va agregar. (insert)
        ```python
        lista_nombres=['jory','nadine','bichota']
        lista_nombres.insert(1,'satan')
        print(lista_nombres)
        ```
    - Esta funcion nos permite eliminar elementos de cualquier pocision de una lista, esta funcion recibe solo el elemento que deseamoseliminar.(remove)
        ```python
        lista=[1,2,3,4,5]
        lista.remove(3)
        print(lista)
        ```
    - Funcion que nos permite dividir en una lista, una cadena 
        ```python
        cadena='hola como tas'
        lista=cadena.split()
        url='www.golle.com/id=7074665'
        id=url.split('=').pop
        print(id)
        ```
        pop almacena el dato que eliminamos, solo debemos almacenarlos en una variable para mostrarlo
        ```python
        lista=[15,12,50]
        eliminado=lista.pop()
        print(eliminado)
        ```




2. funciones creadas

    son funciones que el usuario lo crea para su uso

    pasos para crear una funcion prpopia

    1. hacer uso de la palabra reservada. 

    2. definir un nombre de funcion que describa que tarea va realizar.

    3. establecer los parametros que recibira la funcion entre parentesis.
   
    4. establecer que valor o dato va retornar mi funcion con la palabra reservada return

    observacion: tambien podemos hacer uso de la funcion print para retornar un mensaje.

> exissten dos tiposn de funciones dentro de las funciones creadas
las que no reciben ningun parametro como pop y los que si reciben parametros como print.

``` python
def saludo():
print('hola este es un saludo')

```
¿como hacemos uso de la funcion?
ponemos el nombre de la funcion acompañado de parentesis al final.
```python
saludo()
```
mi funcion con parametros
```python
def mi_print(texto):
    print(texto)

print('print de python')
mi_print('hola este es mi print creado')
```
```python
def suma(a,b):
    total=a+b
    return total
mi_print(suma(45+12)) #==> 57

```
ejemplo
para que se usa esta funcion?
max( ) muestra numero mayor

crear mi propia funcion que haga lo mismo
```python
lista=[12,45,78,3,1]
def mi_max(lista): #===>>> la funcion que estoy creando
    numero_mayor=lista[0]
    for numero in lista:
        if numero > numero_mayor:
        numero_mayor=numero
return numero_mayor
mi_print(mi_max(lista)) #===>>> mi_print es la funcion vacia que cree arriba, donde tiene en parentesis (texto)
```