from bbdd import *

class Tiendas:

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

    def actualizar_negocio(self,id, clave,valor):
        ol=valor
        producto_actualizar=list(filter(lambda obj:obj[clave]==id,negocios))[0].update({clave:valor}) 
        return 'se actualizo'

    def borrar(self, ruc):
        re=list(filter(lambda el:el['ruc']!=ruc,negocios))
        return re

a=Tiendas()
#print(a.gerente(negocios,'Lourdes'))
#print(a.tienda_ctg('bodega'))
#print(a.ruc_nombre())
#print(a.mostrar_negocio(negocios,'Lulu'))
#print(a.mostrar_tiendas())
#print(a.categorias_tienda(negocios))

print(a.eliminar_negocio(1))
print(a.actualizar_negocio('Lulu','nombre','gatuno'))
print(a.mostrar_negocio(2))
#print(a.borrar(2365897412))

# tarea
## otro metodo para crear un nuevo producto
## otro metodo para actu8alizar el horario de atencion
