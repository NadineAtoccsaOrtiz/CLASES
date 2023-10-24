from bbdd import *

class Tiendas:
    def __init__(self,ruc,nombre, categoria,horario_atencion,gerente,):
        #self.id=id
        self.ruc=ruc
        self.nombre=nombre
        self.categoria=categoria
        self.horario_atencion=horario_atencion
        self.gerente=gerente

    def gerente(self,bd_negocios,nombre_gerente):
        c=list(filter(lambda par:par['gerente']==nombre_gerente,bd_negocios))
        return f'''Aqui tienes informacion del gerente que buscaste: 
        ...........................................................................................................................................................................................................
        {c}'''
        
    def tienda_ctg(self,cat):
        b=list(filter(lambda par:par['categoria'][0]==cat,negocios))
        return f'''Las tiendas que estan en categoria {cat}: 
        ..........................................................................................................................................................................................................
        {b}'''
    
    def categorias_tienda(self,bd_negocios):
        res=list(filter(lambda par:len(par['categoria'])>2,bd_negocios))
        return f'''los gerentes que manejan 3 tiendas son los siguientes:
        ...............................................................................................................................................................................................................
        {res}'''

    def ruc_nombre(self):
        nuevo_objeto=list(map(lambda par:{'nombre_gerente': par ['nombre'],'ruc_gerente':par ['ruc']}, negocios))
        return f'''Los gerentes y su ruc: 
        .................................................................................................................................................................................................................
        {nuevo_objeto}'''

    def mostrar_negocio(self, ide):
        g=list(filter(lambda par:par['id']==ide,negocios))
        return f'''Aqui tienes informacion de la tienda que buscaste:
        .................................................................................................................................................................................................................... 
        {g}'''
        
    def mostrar_tiendas(self):
        mensaje=f"""
        Existen {len(negocios)} tiendas.
        las tiendas son:
        ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
        {negocios}
        """
        return mensaje
    
    def eliminar_negocio(self, id):
        negocio_eliminar=negocios.pop(id-1)
        return f"el siguiente producto fue eliminado {negocio_eliminar}"

    def actualizar_negocio(self, id, clave,valor):
        ol=valor
        negocio_actualizar=list(filter(lambda obj:obj[clave]==id,negocios))[0].update({clave:valor}) 
        return 'se actualizo'

    def borrar(self, ruc):
        re=list(filter(lambda el:el['ruc']!=ruc,negocios))
        return re
    def registrar_negocio(self):
        nuevo_id=len(negocios)+1
        negocio_nuevo={
        'id':nuevo_id,
        'ruc':self.ruc,
        'nombre':self.nombre,
        'categoria':self.categoria,
        'horario_atencion':self.horario_atencion,
        'gerente':self.gerente
    }
        registro_negocio=negocios.append(negocio_nuevo)
        return 'producto registrado exitosamente'

    def actualizar_horario(self, id, clave, valor):
        negocios[id-1][clave]=valor
        #actu_hora=list(filter(lambda obj:obj[clave]==dato,negocios))[0].update({clave:valor}) 
        return 'se actualizo el horario'

a=Tiendas(123456789,'panesito','abarrotes,bodega,restaurante',{'dia':'9am-11am','tarde':'5pm-9pm'},'maria')
#print(a.gerente(negocios,'Lourdes'))
#print(a.tienda_ctg('bodega'))
#print(a.ruc_nombre())
#print(a.mostrar_negocio(negocios,'Lulu'))
#print(a.mostrar_tiendas())
#print(a.categorias_tienda(negocios))

# print(a.eliminar_negocio(1))
#print(a.actualizar_negocio('Lulu','nombre','gatuno'))
# print(a.mostrar_negocio(2))
#print(a.borrar(2365897412))

# print(a.registrar_negocio())
# print(a.mostrar_negocio(11))
print(a.actualizar_horario(1,'horario_atencion',{'dia':'7am-12pm','tarde':'3pm-9pm'}))
print(a.mostrar_negocio(2))
# tarea
## otro metodo para crear un nuevo producto
## otro metodo para actu8alizar el horario de atencion
