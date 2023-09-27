# 1. haciendo uso de la poo crear un objeto para la entidad "celular"
class celular: 
    marca='samsung'
    propietario='you'
    color='blue'
    version='A33'

    def llamar(self, nom): 
        contacto=f"llamando a {nom}, de tu lista de contactos."
        return contacto
    def escribir(self, txt, person):  
        texto= f"tu mensaje en whatsapp es <<{txt}>> para {person}."
        return texto
    def abrir_app(self, apk):
        app=f"abriendo {apk} en tu celular."

        return app

respuesta=celular()
print(respuesta.marca)
print(respuesta.llamar("maria"))
print(respuesta.escribir("hola, como estas", "emma"))
print(respuesta.abrir_app("whatsapp"))

# 2. haciendo uso de la poo crear un objeto para la entidad "vehiculo"
class vehiculo: 
    marca='mercedes'
    propietario='you'
    color='rojo'
    serie='bens-865'

    def acelerar(self, km): 
        velocidad= f"vas a {km}km/h de velocidad"
        return velocidad
    def frenar(self,):   
        return "frenaste"
    def girar(self, direcc):
        direccion=f"giraste hacia la {direcc}."
        return direccion

respuesta=vehiculo()
print(respuesta.marca)
print(respuesta.acelerar(40))
print(respuesta.frenar())
print(respuesta.girar("derecha"))

# 3. haciendo uso de la poo crear un objeto para la entidad "avion"
class avion: 
    marca='Boeing'
    propietario='you'
    color='blanco'
    serie='Boeing-865'

    def despegar(self, km): 
        velocidad= f"vas a {km}km/h de velocidad"
        return velocidad
    def aterrizar(self,):   
        return "aterrisaste"
    def girar(self, direcc):
        direccion=f"giraste hacia la {direcc}."
        return direccion

respuesta=avion()
print(respuesta.marca)
print(respuesta.despegar(120))
print(respuesta.aterrizar())
print(respuesta.girar("izquierda"))

# 4. haciendo uso de la poo crear un objeto para un "heroe de dota2"


# leer tkinter, libreriade python para la creacion de interfaces graficas