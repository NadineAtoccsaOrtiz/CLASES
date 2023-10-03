# 1. haciendo uso de la poo crear un objeto para la entidad "celular"
class Celular: 
    marca='samsung'
    propietario='you'
    color='blue'
    version='A33'

    def llamar(self, nom): 
        contacto=f"llamando a {nom}, de tu lista de contactos."
        return contacto
    def escribir(self, txt, person):  
        texto= f"tu mensaje en whatsapp es << {txt} >> para {person}."
        return texto
    def abrir_app(self, apk):
        app=f"abriendo {apk} en tu celular."

        return app

respuesta=Celular()
print(respuesta.marca)
print(respuesta.llamar("maria"))
print(respuesta.escribir("hola, como estas", "emma"))
print(respuesta.abrir_app("whatsapp"))

# 2. haciendo uso de la poo crear un objeto para la entidad "vehiculo"
class Vehiculo: 
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

resp=Vehiculo()
print(resp.marca)
print(resp.acelerar(40))
print(resp.frenar())
print(resp.girar("derecha"))

# 3. haciendo uso de la poo crear un objeto para la entidad "avion"
class Avion: 
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

re=Avion()
print(re.marca)
print(re.despegar(120))
print(re.aterrizar())
print(re.girar("izquierda"))

# 4. haciendo uso de la poo crear un objeto para un "heroe de dota2"

class Heroe: 
    nombre='Abaddon'
    daño='daño: 23'
    vida='vida: 460'
    regeneracion_vida='regeneracion de vida: 2.3'
    armadura='armadura: 3.8'
    velocidad_ataque='velocidad de ataque: 23'
    mana='cantidad de mana: 216'
    regeneracion_mana='regenracion: 0.9'
    habilidades='Habilidades: espiral de niebla, escudo afotico, maldicion del averno'

    def espiral_niebla(self, daño_autoinflingido, daño_curacion, alcance):        
        daño=f'Usaste el ataque << espiral de niebla >>, causando un daño autoinflingido de {daño_autoinflingido}%, daño de curacion de {daño_curacion} y con un alcance de {alcance}.🤯'
        return daño
    def escudo_afotico(self, duracion, radio_explosion, barrera_daño):   
        daño=f'Usaste el ataque << escudo afotico >>, con una duracion de {duracion}, con una radio de explosion de {radio_explosion} y una barrera de daño de {barrera_daño}.🤩'
        return daño
    def maldicion_del_averno(self, duracion, relentizacion, velocidad):
        daño=f'Usaste el ataque << maldicion del averno >>, con una duracion de {duracion}, con una relentizacion de {relentizacion}% y con una velocidad de {velocidad}.😲'
        return daño
    
rpta=Heroe()
print(rpta.nombre)
print(rpta.daño)
print(rpta.vida)
print(rpta.habilidades)

ataque=input('ingresa el ataque: ')
if ataque=='espiral de niebla':
    print(rpta.espiral_niebla(150, 260, 575))
    if ataque=='escudo afotico':
        print(rpta.escudo_afotico(15, 675, 200))
        if ataque=='maldicion del averno':
            print(rpta.maldicion_del_averno(4.5, 60,120 ))
else:
    print('error')

## 5. haciendo uso de la poo crear un objeto para una pc
class Pc:
    marca='hp'
    modelo='pavilion'
    procesador='intel core i7'        
    ram=' 16GB'
    almacenamiento='1TB'
    
    def encendido(self):
        print(f'''Ecendiendo equipo
        .....cargando recursos.....''')
        return 
    def apagado(self):
        print(f'''Apagando el equipo...
        🌐🌀''')
        return 

dev=Pc()
print(dev.marca)
print(dev.procesador)
print(dev.encendido())
print(dev.apagado())

## 6. haciendo uso de la poo crear un objeto para una impresora

class Impresora:
    marca='Epson'
    modelo='g-3456'
    capacidad='capacidad: 5,350 páginas'       
    
    def imprimir(self, colores, hojas):
        impr=f'La impresion esta siendo procesada, la impresion saldra a {colores}, cantidad de hojas: {hojas}.'
        return impr
    def copia(self, colores):
        copiar=(f'''
        La copia esta siendo procesada, 
        ................
        la copia saldra a {colores}.
        ''')
        return copiar
    def escanear(self, format):
        escan=f'Escaneando documento: La hoja escaneada se guardara en fomato {format}, en tus archivos.'
        return escan
de=Impresora()
print(de.marca)
print(de.capacidad)
print(de.imprimir('b/n','10'))
print(de.copia('colores'))
print(de.escanear('pdf'))

## 7. haciendo uso de poo crear un objeto para emiotir una factura

class Factura:
    empres='Distribuidora AZUL E.I.R.L'
    razon_social='CLIENTE: constructora fym'
    ruc_o_dni='20609976285'
    direccion='jr ayacucho 285'
    tipo_moneda='soles'

    def emitir_fac(self, razon, ruc, dire, monto):
        fac=f'''
        FACTURA Nº 345
        ---------------------------
        Razon Social: {razon}
        RUC: {ruc}
        Direccion: {dire}
        Moneda=: Soles
        Monto: {monto}
        
        Gracias por su compra.
        '''
        return fac
    def anular_fac(self, ope, numero_fac):
        anular=f'''
        NOTA DE CREDITO Nº 189
        ---------------------------
        Operacion: {ope}
        Nº de factura: {numero_fac}
        
        Emitiendo NOTA DE CREDITO
        .........................
        '''
        return anular

factura=Factura()
print(factura.empres)

operacion=(input('Ingresa la operacion a realizar:  '))
if operacion=='factura':
    print(factura.emitir_fac('CONSTRUCTORA FYM','20146526','JR Ayacucho 453', 's/ 1,899.52'))
if operacion=='nota de credito':
    print(factura.anular_fac('Anulacion','345'))
else:
    print('error')