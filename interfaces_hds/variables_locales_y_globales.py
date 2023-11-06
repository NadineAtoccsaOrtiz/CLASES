# global, disponible solo dentro de la funcion
# local, disponible ne toda la plicacion
edad=20
nombre='china'
def variable():
    nombre='jory' # local, soloo usada dentro de la funcion
    print(edad) # llamo a la variable local edad
    print (nombre) # variable global dentro de la funcion
# local 
variable()
print(nombre) ## error por que estoy llamando la variable fuera de la funcion

def variable():
    global nombre # declaro mi variable gloobal
    nombre ='jose'
print(nombre) # mi print esta nfuera de la funcion pero ya es posible llamarlo 