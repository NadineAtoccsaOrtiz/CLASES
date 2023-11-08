from rich import *
# class Personas:
#     def __init__(self):
#         self.nombre=None
#         self.edad=None
#         self.sexo=None
#         self.ocupacion=None
#     def datos_persona(self,nombre,edad,sexo,ocupacion):
#         self.nombre=nombre
#         self.edad=edad
#         self.sexo=sexo
#         self.ocupacion=ocupacion
#     def hablar(self,idioma):
#         return idioma
    
# class Estudiante:
#     def hacer_tareas(self,curso):
#         return f''' tarea en el curso {curso}'''
# class Trabajador:
#     def trabajo(self,actviidad):
#         return f''' realizar {actviidad}. '''

# maria=Personas()



##########################################################
class Personas:
    def __init__(self,nombre:str,edad:int,sexo:str):
        self.nombre=nombre
        self.edad=edad
        self.sexo=sexo

    def comer(self, plato_favorito):
        return f'yo {self.nombre} estoy comiendo mi {plato_favorito}'
    
    def cagar(self):
        return 'pipi popo'


class Estudiante(Personas):
    def __init__(self,nombre:str,edad:int,sexo:str,carrera:str):
        super ().__init__(nombre,edad,sexo) 
        self.ocarrera=carrera     # para decirles cuales datos hereda de la clase padre
    def estudiar(self):
        return 'estoy estudiando poo'

class Trabajador(Personas):
    def __init__(self,nombre:str,edad:int,sexo:str,profesion:str):
        super ().__init__(nombre,edad,sexo) 
        self.profesion=profesion   
    
    def trabajar(self):
        return 'estoy trabajando'


maria=Estudiante('maria',17,'femenino','arquitectura')
print(f'[bold blue]'+maria.comer('arroz con pollo'))
print(f'[bold blue]'+maria.cagar())
print(f'[bold blue]'+maria.estudiar())

fer=Trabajador('fernando',36,'masculino','secretario')
print(f'[bold blue]'+fer.comer('lomo saltado'))
print(f'[bold blue]'+fer.cagar())
print(f'[bold blue]'+fer.trabajar())