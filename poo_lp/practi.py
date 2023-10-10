class Laptop:
    tipo='Computadora portátil'
    tamaño='13.3 o 14 pulgadas'


    def __init__(self, marca, procesador, ram, sdd, almacenamiento):
        self.marca=marca
        self.procesador=procesador
        self.ram=ram
        self.sdd=sdd
        self.almacenamiento=almacenamiento

    

    
    def prender(self, ):
        encender=f'''ENCENDIENDO LA PC
        .............................................'''
        return encender
    def apagar(self, ):
        apagado=f'''APAGANDO EL EQUIPO
        .............................................'''
        return apagado
    def app(self, apk):
        abrir_app=f'abriendo {apk} en la pc.'
        return abrir_app
    def info(self, marca, procesador, ram, sdd, almacenamiento):
        respuesta=f'''
        ___________________________
        tipo: {self.tipo}
        marca | modelo | ram | t.disco | almacenamiento
        {self.marca}{self.modelo}{self.ram}{self.sdd}{self.almacenamiento}
        ___________________________'''
        return respuesta


equipo1=Laptop('lg','intel','8gb','128 gb','1T')
print(equipo1.tipo)
print(equipo1.prender())
print(equipo1.app('canva'))


equipo2=Laptop('hp','intel','8gb','128 gb','1T')
print(equipo2.tipo)
print(equipo2.apagar())
print(equipo2.app('whatsapp'))

equipo3=Laptop('hp','intel','8gb','128 gb','1T')
print(equipo3.tipo)
print(equipo3.info())
