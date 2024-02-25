from flask import Flask
from sqlalchemy import and_, or_
from hashlib import sha256

from alchemyClasses import db
from alchemyClasses.Usuario import Usuario
from alchemyClasses.Pelicula import Pelicula
from alchemyClasses.Renta import Renta
from model.model_usuario import actualiza_nombre_usuario, eliminar_usuario
from model.model_pelicula import actualiza_nombre_pelicula, eliminar_pelicula
from model.model_renta import actualiza_fecha_renta, eliminar_renta_usuario, eliminar_renta_pelicula, eliminar_renta


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://lab:Developer123!@localhost:3306/lab_ing_software'
app.config.from_mapping(
    SECRET_KEY='dev'
)
db.init_app(app)

## Funciones auxiliares repetitivas
def selecionar_tabla():
    print("Seleccione la tabla donde desea realizar la operación")
    print("1.- Usuarios")
    print("2.- Peliculas")
    print("3.- Rentas")
    opcion = input()
    return opcion

def actualizar_nombre_opcion():
    print("Ingrese el id del registro a cambiar")
    id = input()
    print("Ingrese el nuevo valor")
    nuevo_valor = input()
    return id, nuevo_valor

def ver_registros():
    opcion= selecionar_tabla()
    if opcion == "1":
        usuarios = Usuario.query.all()
        for usuario in usuarios:
            print(usuario)
    elif opcion == "2":
        peliculas = Pelicula.query.all()
        for pelicula in peliculas:
            print(pelicula)
    elif opcion == "3":
        rentas = Renta.query.all()
        for renta in rentas:
            print(renta)
    else:
        print("No es una opción valida")


def filtrar_por_id():
    opcion= selecionar_tabla()
    print("Ingrese el id del registro que desea actualizar")
    id = input()
    if opcion == "1":
        resultado = Usuario.query.filter(Usuario.idUsuario == id).first()
    elif opcion == "2":
        resultado = Pelicula.query.filter(Pelicula.idPelicula == id).first()
    elif opcion == "3":
        resultado = Renta.query.filter(Renta.idRentar == id).first()
    else:
        print("No es una opción valida")
        exit()
    
    if resultado is not None:
        print(resultado)
    else:
        print("No se encontro el registro")



def actualizar_registro():
    print("Si desea actualizar la fecha de renta, favor de poner la fecha con el formato AAAA-MM-DD, favor de omitir la hora.")
    opcion= selecionar_tabla()
    id, nuevo_valor = actualizar_nombre_opcion()
    if opcion == "1":
        actualiza_nombre_usuario(id, nuevo_valor)
    elif opcion == "2":
        actualiza_nombre_pelicula(id, nuevo_valor)
    elif opcion == "3":
        actualiza_fecha_renta(id, nuevo_valor)
    else:
        print("No es una opción valida")

def eliminar_registro_usuario(todos):
    if todos == "TODO":
            usuarios = Usuario.query.all()
            for usuario in usuarios:
                eliminar_renta_usuario(usuario.idUsuario)
                eliminar_usuario(usuario.idUsuario)
            print("Todos los usuarios han sido eliminados")
    else:
            print("Ingrese el id del usuario que desea eliminar")
            id = input()
            eliminar_renta_usuario(id)
            eliminar_usuario(id)

def eliminar_registro_pelicula(todos):
    if todos == "TODO":
            peliculas = Pelicula.query.all()
            for pelicula in peliculas:
                eliminar_renta_pelicula(pelicula.idPelicula)
                eliminar_pelicula(pelicula.idPelicula)
            print("Todas las peliculas han sido eliminadas")
    else:
            print("Ingrese el id de la pelicula que desea eliminar")
            id = input()
            eliminar_renta_pelicula(id)
            eliminar_pelicula(id)
            

def eliminar_registro_renta(todos):
    if todos == "TODO":
            rentas = Renta.query.all()
            for renta in rentas:
                eliminar_renta(renta.idRentar)
            print("Todas las rentas han sido eliminadas")
    else:
            print("Ingrese el id de la renta que desea eliminar")
            id = input()
            eliminar_renta(id)
            print("Renta eliminada con éxito")

def eliminar_registro():
    opcion= selecionar_tabla()
    print("Si desea eliminar todos los registros, favor de escribir 'TODO'")
    print("Tenga en cuenta que al borrar un usuario o pelicula se borraran todas las rentas asociadas a el.")
    todos = input()
    if opcion == "1":
        eliminar_registro_usuario(todos)
    elif opcion == "2":
        eliminar_registro_pelicula(todos)
    elif opcion == "3":
        eliminar_registro_renta(todos)
    else:
        print("No es una opción valida")


if __name__ == '__main__':
    with app.app_context():
        print("Sea bienvenido al sistema de renta de peliculas")
        print("Seleccione una opcion:")
        print("1.- Ver registors de una tabla")
        print("2.- Filtrar registros por id")
        print("3.- Actualizar nombre de registros*")
        print("4.- Eliminar un registro por id o todos los registros")
        print("5.- Salir")
        print("*En caso de rentas solo podra modificar la fecha de renta")
        print("Para selecionar una opción favor de escribir el numero en terminal.")
        opcion = input()

        if opcion == "1":
            ver_registros()
        elif opcion == "2":
            filtrar_por_id()
        elif opcion == "3":
            actualizar_registro()
        elif opcion == "4":
            eliminar_registro()
        elif opcion == "5":
            print("Adios")
            exit()
        else:
            print("No es una opción valida, el sistema se cerrara.")
            exit()
