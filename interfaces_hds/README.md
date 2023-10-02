# leer tkinter, libreriade python para la creacion de interfaces graficas
Tkinter es una librería del lenguaje de programación Python y funciona para la creación y el desarrollo de aplicaciones de escritorio. Esta libreria para crear interfaz grafica en python facilita el posicionamiento y desarrollo de una interfaz gráfica de escritorio con Python, es decir, nos enseña como hacer interfaz grafica en python . Tkinter es el paquete estándar de Python para interactuar con Tkt.

Funcionalidades de Tkinter: 
Tkinter ofrece una amplia gama de widgets, que son los elementos visuales utilizados en 
una interfaz gráfica. Estos incluyen botones, etiquetas, cajas de texto, cuadros de selección 
y muchos más. Además, Tkinter permite personalizar la apariencia de estos widgets, controlar
 la disposición de los elementos en la ventana y gestionar eventos como el clic de un botón o 
 la entrada de texto.

Widgets: 
Los widgets son elementos visuales utilizados en las interfaces gráficas. Algunos
 ejemplos comunes son botones, etiquetas, cuadros de texto y casillas de verificación.

Personalización de widgets: 
Tkinter permite cambiar la apariencia de los widgets, como el color de fondo, la fuente 
y el tamaño del texto, entre otros. Esto permite adaptar la interfaz a las necesidades y 
preferencias del usuario.

Disposición de elementos: Tkinter ofrece diferentes métodos para organizar los widgets en
la ventana de la aplicación. Algunas opciones incluyen cuadrícula, paquetes y enrejado.

Gestión de eventos: 
Los eventos son acciones realizadas por el usuario, como hacer clic en 
un botón o escribir en un cuadro de texto. Tkinter permite asociar funciones a estos eventos 
para que se ejecuten cuando ocurran.

## ejemplo
```python
from tkinter import *
from tkinter import ttk
```

# modo de uso

Para usar Tkinter en Python, primero debes asegurarte de que Tkinter está instalado en tu computadora. En la mayoría de las distribuciones de Python, Tkinter ya está incluido en la instalación estándar de Python, pero si no lo tienes, deberás instalarlo.

Una vez que tienes Tkinter instalado, puedes comenzar a crear tu interfaz gráfica de usuario utilizando Python y Tkinter. A continuación, te proporcionamos un ejemplo básico para que puedas empezar:

Este código crea una ventana principal con el título «Primer programa con Tkinter. Dentro de la ventana, se agrega una etiqueta con el texto «¡Bienvenido a mi Canal!».

En este ejemplo de como usar tkinter en python, se importa como tk para reducir la cantidad de caracteres necesarios para hacer referencia a las funciones y widgets de Tkinter.

El tk.Tk() crea una nueva ventana principal, que se almacena en la variable root. La etiqueta se crea utilizando tk.Label(), y se pasa el texto que se mostrará en la etiqueta como un parámetro. La etiqueta se agrega a la ventana principal utilizando el método pack().

El botón se crea utilizando tk.Button(). El parámetro text se utiliza para especificar el texto que aparecerá en el botón, y command se utiliza para especificar la función que se ejecutará cuando se haga clic en el botón. En este caso, la función es root.quit, que cierra la ventana principal. El botón se agrega a la ventana principal utilizando el método pack().

Finalmente, root.mainloop() se utiliza para iniciar el bucle principal de la aplicación. Este bucle procesa los eventos de la ventana, como hacer clic en un botón o cerrar la ventana.



# ejemplo practico -- main.py
