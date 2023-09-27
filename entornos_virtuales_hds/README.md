# ENTORNOS VIRTUALES 
Son pequeños espacios de trabajo aislados para poder gestionar 
>  PYENV: No es un entorno virtual, es un controlador o manejador de versiones de python.
> CONDA: 
> PIPENV: Creador de entornor vistuales desfasado (ya no se usa). 

para usar las herramientas se necesita un manejador de paquetes,comando que permite instalar distintos paquetes dentro del ordenador, o proyectos

- poetry
- virtualenv
- venv: viene de manera predeterminada con el pauqte de python

1. para crear una maquina virtual
nos ubicamos en la carpeta que deseamos crear el entorno virtual
ingresamos con cd y la ruta del archivo 
ejemplo:
cd <ruta del archivo>
```bash
cd nombre_carpeta/entorno_uno
```
2. creamos el entorno virtual con el siguiente comando
```bash
python -m venv <nombre de nuestro entorno>
#ejemplo
python -m venv mi _entorno
```
3. abrimos nuevo terminal, nos ubicamos dentro de la carpeta de mi entorno, ejecutamso el comando anterior, una vez finalizado,
abrimos la terminal de git bash, y escribimos lo siguiente

```bash
source venv_uno/Scripts/activate 
```
> NOTA:
> 
> en caso de que no corra en bash, podemos usar powershell, seleccionamos powershell como terminal predeterminado ejecutar el siguiente comando
```bash
venv/Scripts/Activate.ps1
```
## PARA INSTALAR PAQUETES N NUESTRO ENTORNO
1. primero verificamos que no tengamos el paquete instalado y lo listamos con el siguiente comando, debemos tener activado nuestro entorno virtual primero
```bash
pip list
```
2. luego instalaremos con el siguiente comando 
```bash
pip install <nombre del paquete>
#ejemplo
pip intsall pandas
```
3. deactivate para desactivar el venv

> nota
> para powershell
> escribir las iniciales de la carpeta y clic en tap(la tecla de dos flechas) para autocompletar la ruta del archivo

para activar los scripts y evitar errores
abrir y ejecutar como administrador el powershell
dentro 
```bash
Get-ExecutionPolicy
```

para quitar la restriccion
```bash
Set-ExecutionPolicy Unrestricted
```

> clic derecho propiedades, activar uso de contrl c
