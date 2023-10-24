## lambda es una funcion que se autoejecuta
# hola=lambda a,b:print(a+b)
# funcion normal
# def suma(a,b):
#     print(a+b)
# suma(2,6)

# hola(10,20)

## if ternario
# ternario='soy verdad ternario'if True else 'soy falso ternario'
# print(ternario)

## if normal
# if True:
#     print('soy verdad')
# else:
#     print('soy falso')


## programador pythonico, metodo


## filter explicacion
lista_alumnos=[
    {
        'nombre':'edwin',
        'edad':15,
        'hobbie':'danza',
        'flaquita':'melody'
    },

    {
        'nombre':'del mar',
        'edad':30,
        'hobbie':'saltar',
        'flaquita':'sami'
    },

    {
        'nombre':'orlando',
        'edad':14,
        'hobbie':'ponchar',
        'flaquita':'melody'
    },

    {
        'nombre':'jory',
        'edad':50,
        'hobbie':'aplicar',
        'flaquita':'sami'
    },

    {
        'nombre':'hans',
        'edad':13,
        'hobbie':'quemarse',
        'flaquita':'hermana'
    }
]
print(f'todos mis alumnos {lista_alumnos}')
fans_melody=list(filter(lambda par:par['flaquita']=='melody',lista_alumnos))
print(f'los que quieren con melody {fans_melody}')



fans_melody=list(filter(lambda par:par['edad']>49,lista_alumnos))
print(f'los que quieren con melody {fans_melody}')

## averiguar como hacer para que en mi objeto solo me muestre el nombre y flaquita 

## map 

nuevo_objeto=list(map(lambda par:{'nombre_alumno': par ['nombre'],'germita':par ['flaquita']}, lista_alumnos))
print(nuevo_objeto)


## tarea
# 1. crear una lista con 10 objetos que contengan los datos de las tiendas comerciales 
#  ejemplo 
tiendas = [
    {
        'ruc':2060156458,
        'nombre':'el pichito',
        'categoria':['abarrotes', 'bodega'], # va ser un array, puede devolver dos funciones o uno o tres
        'horario_atencion':{
            'dia': '7am-12pm',
            'tarde': '2pm - 8pm'
                        },
        'gerente': ' nadine' # va ser un objeto y va devolver dos 
    }
]
## observacion: las categorias seran 4
# abarrotes 
# farmacia
# bodega
## observacion: los gerentes solo popdran ser los siguientes: 
## edwin
# china
# crhistian
# nadine

# realizar lo siguientes
# 1. crear unna clase que tenga los siguientes metodos o casos de uso
# - crear un metodo  que me filtre las tiendas que tienen cada gerente pasandole el parametro de cada uno: por ejemplo si digo edwin me muestra las tiendas de edwin
# - crear un metodo que muestre los negocios que tienen mas de dos categorias
# - crear un metodo que me muestre solo el nombre y el ruc de las tiendas
