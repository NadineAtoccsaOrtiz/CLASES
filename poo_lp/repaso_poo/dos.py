from rich import *
## repaso de programacion orientada a objetos
class Mascota:
    def __init__(self): 
        self.nombre=None 
        self.edad=None
        self.tipo_animal=None
    def hablar(self,sonido):
        return sonido
    def datos_mascota(self,nombre,edad,tipo_animal):
        self.nombre=nombre
        self.edad=edad
        self.tipo_animal=tipo_animal

# class Perro:
#     # atributos de clase
#     especie ='animal'
#     # atributos de instancia
#     def __init__(self): # para asociar la clase con  el metodo, init hace que se ejcute automaticamente
#         self.nombre=None # se autoinicializa
#         self.edad=None # viene atrvez del parametro
#     # metodos -> funciones o acciones que puede realiozar mi clase
#     def ingresa_dato(self,nombre,edad):
#         self.nombre=nombre
#         self.edad=edad


# un objeto se crea apartir de instanciar
# se instancia almacenando en una varible la clase
# boby=Perro() # estamos instanciando.. mi objeto es boby
# print(boby.hablar())
# print(boby.especie)
# boby.ingresa_dato('edwin',14)
# print(boby.nombre)

class Perro(Mascota):
    def atacar(self):
        return 'ladra y muerde'
class Gato(Mascota):
    pass

perro_boby=Perro()
perro_boby.datos_mascota('boby',14,'perro')
print(f'[bold blue]'+perro_boby.nombre+' '+perro_boby.tipo_animal)
print(f'[bold blue]'+perro_boby.hablar('guau guau'))
print(f'[bold blue]'+perro_boby.atacar())

gato_persa=Gato()
gato_persa.datos_mascota('persa',10,'gato')
print(f'[bold green]'+gato_persa.nombre+' '+gato_persa.tipo_animal)
print(f'[bold green]'+gato_persa.hablar('miau miau'))

