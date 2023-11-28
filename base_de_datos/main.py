# from hola import *
# def suma(x,y):
#     return x+y
# pregunta=input("ingresa un numero")
# print(suma(int(pregunta),10))
# if __name__ == "__main__": ## para autoejecutrar funciones
#     print(5,8)
### imprime el nombre del archivo actual

# sqlite == sistema gestor de base de datos basado en un archivo/s donde se almacena todo
from sqlite3 import *
def crearconexion():
    conectar=connect("./base_de_datos/tecnologico.bd")
    conectar.commit()
    conectar.close()
    
def creartablaAlumno():
    conectar=connect("./base_de_datos/tecnologico.bd")
    cursor=conectar.cursor()
    sentencia="""
        CREATE TABLE IF NOT EXISTS Alumnos(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT(250),
            edad INTEGER
        )
    """ ## Siempre en plurarl y enpieza en mayusculas
    cursor.execute(sentencia)
    conectar.commit()
    conectar.close()
if __name__ == "__main__":
    creartablaAlumno() 
    
def creartablaCurso():
    conectar=connect("./base_de_datos/tecnologico.bd")
    cursor=conectar.cursor()
    sentencia="""
        CREATE TABLE IF NOT EXISTS Cursos(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT(250),
            id_alumnos INTEGER,
            FOREIGN KEY(id_alumnos) REFERENCES Alumnos(id)
        )
    """ 
    cursor.execute(sentencia)
    conectar.commit()
    conectar.close()
if __name__ == "__main__":
    creartablaCurso()


def insertarAlumno(nombre,edad):
    conectar=connect("./base_de_datos/tecnologico.bd")
    cursor=conectar.cursor()
    sentencia=f"INSERT INTO Alumnos (nombre,edad) VALUES ('{nombre}',{edad})"
    cursor.execute(sentencia)
    conectar.commit()
    conectar.close()

def insertarAlumnos(lista):
    conectar=connect("./base_de_datos/tecnologico.bd")
    cursor=conectar.cursor()
    sentencia=f"INSERT INTO Alumnos (nombre,edad) VALUES (?,?)"
    cursor.executemany(sentencia,lista)
    conectar.commit()
    conectar.close()
    
# if __name__ == "__main__":
    # insertarAlumno('jory',20)
    # insertarAlumno('china',12)
    # alumn=[
    #     ('jory',50),
    #     ('china',60),
    #     ('nadine',18),
    #     ('mochi',15),
    #     ('viuda negra',300)
    #     ]
    
    # insertarAlumnos(alumn)

def actualizarAlumno(id, nombre, edad):
    conectar = connect("./base_de_datos/tecnologico.bd")
    cursor = conectar.cursor()
    sentencia = f"UPDATE Alumnos SET nombre = '{nombre}', edad = {edad} WHERE id = {id}"
    cursor.execute(sentencia)
    conectar.commit()
    conectar.close()

# def actualizarCurso(id, nombre, id_alumno):
#     conectar = connect("./base_de_datos/tecnologico.bd")
#     cursor = conectar.cursor()
#     sentencia = f"UPDATE Cursos SET nombre = '{nombre}', id_alumnos = {id_alumno} WHERE id = {id}" 
#     cursor.execute(sentencia)
#     conectar.commit()
#     conectar.close()

def eliminarAlumno(id):
    conectar = connect("./base_de_datos/tecnologico.bd")
    cursor = conectar.cursor()
    sentencia = f"DELETE FROM Alumnos WHERE id = {id}"
    cursor.execute(sentencia)
    conectar.commit()
    conectar.close()

def eliminarCurso(id):
    conectar = connect("./base_de_datos/tecnologico.bd")
    cursor = conectar.cursor()
    sentencia = f"DELETE FROM Cursos WHERE id = {id}"
    cursor.execute(sentencia)
    conectar.commit()
    conectar.close()

if __name__ == "__main__":
    actualizarAlumno(1,'jory',250)
    eliminarAlumno(28)

## tarea, actualizar y eliminar alumnos


