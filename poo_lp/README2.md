# ATRIBUTOS DE CLASE Y ATRIBUTOS DE INSTANCIA

## Diferencia entre un atributo de clase y un atributo de instancia
> Los atributos de instancia pertenecen a dicha instancia, es decir, podemos crear otras instancias provenientes de la misma clase, con distintos atributos.

> Por otro lado los atributos de clase pertenecen a dicha clase y por tanto siempre que dicha clase sea creada, se inicializará con el mismo atributo de clase. Que se puede cambiar en todas las instancias, simplemente llamando a la clase. 

## EJEMPLO CELULARES 📱
```python
class Celular:
    # atributos tipo clase
    #que son iguales para todos los objetos 
    # que se creen
    familia='Smart Fhone'
    # se sobre escribe cuando coincide el mismo nombre de variable


    # atributos de instancia
    # son atributos propios del objeto
    # creamos una funcion inicializadora
    def __init__(self, marca, modelo, imei, nrocelular):
        self.marca=marca
        self.modelo=modelo
        self.imei=imei
        self.nrocelular=nrocelular
    # funcionalidades
    def llamar(self, destino):
        return f'llamando a {destino}'

    #objeto cecular jory
llamandojory=Celular('poco','x5','723576456','67867867876')
#instanciando mi clase - creadon mi objeto celular
print(llamandojory.marca)
print(llamandojory.familia)
print(llamandojory.llamar('china'))

#objeto celular nadine
llamandonadine=Celular('alcatel','basic','715345646','6424564566')

print(llamandonadine.marca)
print(llamandonadine.familia)
print(llamandonadine.llamar('ollanta'))
```

