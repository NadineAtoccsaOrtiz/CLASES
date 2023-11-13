class Vehiculo:
    def __init__(self,marca:str,modelo:str,color:str,ruedas:int):
        self.marca=marca
        self.modelo=modelo
        self.color=color
        self.ruedas=ruedas
    def prender(self):
        return 'encendiendo motores'
    def apagar(self):
        return 'apagando vehiculo'
    def avanzar(self,orientacion):
        return f'estas llendo hacia la {orientacion}'
    def retroceder(self):
        return 'estas llendo en retro'

class Auto(Vehiculo):
    def __init__(self,marca:str,modelo:str,color:str,ruedas:int,rpm:int):
        super ().__init__(marca,modelo,color,ruedas) 
        self.rpm=rpm   

    def nitro(self,rpm):
        return 'a toda velocidad a {rpm} rpm'

class Omnibus(Vehiculo):
    def __init__(self,marca:str,modelo:str,color:str,ruedas:int,numero_asientos:int):
        super ().__init__(marca,modelo,color,ruedas) 
        self.numero_asientos=numero_asientos 
    
    def recojer_pasajero(self):
        return 'suba'


mercedes=Auto('mercedes','benz','rojo','4',2000)
print(mercedes.prender())
print(mercedes.apagar())
print(mercedes.avanzar('izquierda'))
print(mercedes.retroceder())


bus=Omnibus('bus','jshgf','amarillo',6,10)
print(bus.prender())
print(bus.apagar())
print(bus.avanzar('derecha'))
print(bus.retroceder())