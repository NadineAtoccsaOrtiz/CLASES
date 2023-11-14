# vamos a crear las constantes para el tema oscuro, no se modifican por eso ya no son variables, se le conoce como constante, cuando el dato es cambiante deja de ser una simple variable y debe ir en mayuscula.
COLOR_FONDO_NEGRO='#1a1b28' # adobe color o color picker para el codigo de colores
COLOR_TEXTO_NEGRO='white'
COLOR_BOTONES_ESPECIAL_NEGRO="#52c9dc"
COLOR_BOTON_NEGRO='#1e2435'
COLOR_CAJA_TEXTO_NEGRO='#1a1b28'

# constantes para el tema claro 
COLOR_FONDO_LIGHT='#ffffff' # adobe color o color picker para el codigo de colores
COLOR_TEXTO_LIGHT='black'
COLOR_BOTONES_ESPECIAL_LIGHT='#52c9dc'
COLOR_BOTON_LIGHT='#f2f8fc'
COLOR_CAJA_TEXTO_LIGHT='#ffffff'


# funcion que nos permite centrar nuestra pantalla
def centrar_ventana(ventana,ancho_ventana,largo_ventana):
    pantalla_ancho=ventana.winfo_screenwidth() # quiero la referencia del ancho de mi ventana (toda la pantalla) almacena el ancho de la ventana padre
    pantalla_largo=ventana.winfo_screenheight() # tenemos que dividir entre dos e igual lo que 
    x=int((pantalla_ancho/2)-(ancho_ventana/2))
    y=int((pantalla_largo/2)-(largo_ventana/2))
    return ventana.geometry (f'{ancho_ventana}x{pantalla_largo}+{x}+{y}')
