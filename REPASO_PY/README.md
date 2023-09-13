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
el resultado es , mundomundomundohola 
```
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

## 5. FUNCIONES
## 6. controles de flujo

