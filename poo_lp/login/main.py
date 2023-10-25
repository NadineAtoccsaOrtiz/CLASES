from bd import * # la variable usuario estara disponible en este archivo

class Usuario:

    def __init__(self,dni,nombre, fecha_nacimiento,edad,usuario,password):
        self.dni=dni
        self.nombre=nombre
        self.fecha_nacimiento=fecha_nacimiento
        self.edad=edad
        self.usuario=usuario
        self.password=password
    
    def edad(self):
        pass #hoy=
    
    def actualizar_edad(self,clave,valor):
        for user in usuarios:
            if user['dni']== self.dni:
                user[clave]= valor
        return 'se actualizo'
        

    def ver_usuario(self,dato):
        g=list(filter(lambda par:par['dni']==dato,usuarios))
        return f'''Aqui tienes informacion para el dni {dato}
        ...
        {g}'''
    def verificar_user(self,usuario_buscar):
        for user in usuarios:
            if user['usuario'] == usuario_buscar:
                return 'Usuario si existe.'
        return 'Usuario no encontrado en los registros.'

    def validar(self, usuario, password):
        for user in usuarios:
            if user['usuario']==usuario:
                if user['password']==password:
                    return 'Usuario y contraseña correctos, bienvenido'
        return 'Usuario o contraseña invalidos'
        
        pass
b=Usuario(75248698,'Maria','10/02/2005','','maria@gmail.com','m1234')
# metodo que sabiendo la fecha de nacimiento me va generar la edad
# crear clase para usuario, debera tener los siguientes metodos
# actualizar edad del usuario
# verificar si usuario esta registrado o existe en mis registros
# validar usuario y password

print(b.actualizar_edad('edad','17'))
print(b.actualizar_edad(75248698,'edad',''))
print(b.validar('maria@gmail.com','m1234'))
print(b.ver_usuario(75248698))
print(b.verificar_user('maria@gmail.com'))