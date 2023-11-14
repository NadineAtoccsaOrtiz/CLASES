variable='4+2'
print(eval(variable)) 
## eval convierte un texto a una expresion matematica
## no reconoce la operacion de porcentaje (%)
##para ello tenenios que haCER LA OPERACION DE OTRA MANERA
var='12*2/100' 
vari='12*4%'
res=vari.replace('%','/100')
print(eval(res))

## para no mostrar el,ultimo valor
hola='j123456789'
print(hola[:-1])