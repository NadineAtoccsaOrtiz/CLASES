## casos de uso 
## historias de usuario 
## product ower
## baclog
## mvp 
## prototipos de mierda 
## averiguar formas normales de bbdd (normalizacion de bbdd)

## ejemplo
# personas=[
#     {
#         'id':1,
#         'nombre':'jory apellido',
#         'categoria':'proveedor'
#     }
# ]

# personas=[
#     {
#         'id':2,
#         'nombre':'jcristian se bautiza en el rio',
#         'categoria':'cliente'
#     }
# ]

# personas=[
#     {
#         'id':.3,
#         'nombre':'jchinita',
#         'categoria':'propietario'
#     }
# ]

## cometar crtl + k + c
## descomentar crtl + k + u

## entidad o entitis
#base de datos sobre lo que voy a trabajar 
## crear sistemna para gestion de productos o control de stock 

productos=[
    {
        'id':1,
        'nombre':'arroz',
        'codigo':'2023-A',
        'descripcion':'costeño costal x 100 kg',
        'stock':5,
        'unidad':'costales',
        'precio':125,
        'moneda':'soles'
    }
]

## casos de uso
class Producto:
    ## atributos de clase
    ## moneda = 'soles'


    ## atribustos de instancia
    def __init__(self, codigo, nombre, descripcion, stock, unidad, precio, moneda='soles',):
        self.codigo=codigo
        self.nombre=nombre
        self.descripcion=descripcion
        self.stock=stock
        self.unidad=unidad
        self.precio=precio
        self.moneda=moneda


    ## creacion de metodos
    def mostrar_productos(self):
        mensaje=f"""
        tienes {len(productos)} productos
        los productos son:
        {productos}
        """
        return mensaje
    def mostrar_producto(self, id):
        producto_buscar=productos[id-1] ## en mis prodcutos empeiza de 0 y el id es 1, por eso id - 1 para que me jueste mi primer producto
        pass

    def registrar_producto(self):
        nuevo_id=len(productos)+1
        producto_nuevo={
            "id":nuevo_id,
            'codigo':self.codigo,
            "nombre":self.nombre,
            'descripcion':self.descripcion,
            'stock':self.stock,
            'unidad':self.unidad,
            'precio':self.precio,
            'moneda':self.moneda
        }
        registro_producto=productos.append(producto_nuevo)
        return 'producto registrado exitosamente'

    def eliminar_producto(self, id):
        producto_eliminar=productos.pop(id-1)
        return f"el siguiente producto fue eliminado {producto_eliminar}"

    def actualizar_producto(self, id, clave, valor):
        ol=valor
        producto_actualizar=list(filter(lambda obj:obj[clave]==id,productos))[0].update({clave:valor}) ## donde dice objet le puedo poner cualquier nombre, 
        # no necesariamente se tiene que llamar objet, es como una nueva variable donde se captura o guarda los prdoductos filtrados
        
        # productos[id-1][clave]=valor
        return 'se actualizo'

## metodod funcional filter, filtra o retorna un lemento que sea true de una lista
## funciones autoejecutadas o anonimas en puthon, se les conoce como funciones lambda
## lambda es una funcion anonima
## su uso o estructura
## lambda a,b : return a+b, el nombre de la funcion es lambda, los parametros a,b y el resultado return
# es una funcion en una sola linea, se va ejecutar automaticamente sin llamarla, 
## si quiero ejecutar esa funcion suma=lambda a,b : return a+b y poder llamar a la variable 
## suma(3,4) ## muestra 7
## no se puede usar en una clase o metodos de un objeto, solo para basico
## lista funcion para crear lista m=list('hola) me devuelve ['h','o','l','a']
## averiguar sobre programacion funcional en python

prod=Producto('2023-b','aceite', 'extra virgen',2, 'botella x litro', 12.5)
print(prod.registrar_producto())
print(prod.mostrar_productos())
print(prod.actualizar_producto(125,'precio','130'))
print(prod.mostrar_productos())
# print(a.actualizar_alumno(1,clave='edad',valor='aceite'))