from rich import print 
from rich.markdown import Markdown
edad=12
respuesta='[bold blue] es mayor de edad' if edad >17 else '[italic underline]es menor de edad'

texto='''
# titulo
parrafo
```
bash
git commit -m "cuerpo del commit"
```
*lista

*lista
> info valiosa
{}

'''.format(respuesta)

mostrar_markdown=Markdown(texto)
print(mostrar_markdown)


## cambiar python que tenemos dentro de script en el entorno, clic enn version python, seleccionar interprete