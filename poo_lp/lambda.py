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
        'flaquita':'msami'
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