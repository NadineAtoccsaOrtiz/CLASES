from bd import * # la variable usuario estara disponible en este archivo

class Usuario:

    # def __init__(self,dni,nombre, fecha_nacimiento,edad,usuario,password):
    #     self.dni=dni
    #     self.nombre=nombre
    #     self.fecha_nacimiento
    #     self.edad=edad
    #     self.usuario=usuario
    #     self.password=password
    
    def edad(self):
        pass #hoy=
    
    def actualizar_edad(self):
        
        pass

    def ver_usuario(self,dni):
        g=list(filter(lambda par:par['dni']==dni,usuarios))
        return f'''El usuario si existe:
        ...
        {g}'''
        return 'el usuario no existe'

    def validar(self, usuario):
        # usuario=
        pass
b=Usuario()
# metodo que sabiendo la fecha de nacimiento me va generar la edad
# crear clase para usuario, debera tener los siguientes metodos
# actualizar edad del usuario
# verificar si usuario esta registrado o existe en mis registros
# validar usuario y password

print(b.ver_usuario(75248696))