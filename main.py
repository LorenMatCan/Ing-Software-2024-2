### Aqui se hara todo lo relacionado con el punto número 1 de la práctica.
### FUnciones para manejar la base de datos usando apuntadores de pyMySQL.

import pymysql.cursors
import random  #Para generar un número aleatorio para todo aquella sección que requiera algo único.
from datetime import datetime

db = pymysql.connect(host='localhost',
                             user='lab',
                             password='Developer123!',
                             database='lab_ing_software')

cursor = db.cursor()

### Funciones para añadir datos a la base de datos.

def add_user (nombre, apPaterno, apMaterno, password, email=None,profilePicture=None,superUser=None):
    if email is None:
        email = str(random.randint(100000, 999999)) + "place_holder"+"@gmail.com"    
    sql = "INSERT INTO usuarios (nombre, apPat, apMat, password, email,profilePicture,superUser) VALUES (%s, %s, %s, %s, %s,%s,%s)"
    cursor.execute(sql, (nombre, apPaterno, apMaterno, password, email,profilePicture,superUser))
    db.commit()


def add_movie (nombre, duracion, inventario, genero=None):
    sql = "INSERT INTO peliculas (nombre, genero, duracion, inventario) VALUES (%s, %s, %s, %s)"
    cursor.execute(sql, (nombre, genero, duracion, inventario))
    db.commit()


### ES necesraio que el usuario ponga bien la fecha de renta, separando los valores con guiones.
### Iniciando por el año, mes y día.
### Ejemplo: "2021-10-10"
def add_rent (correo, titulopelicula, fecha_renta, dias_de_renta=5, estatus=0):
    ### revismaos que sea un número de usuario valido
    sql = "SELECT * FROM usuarios WHERE email= %s"
    cursor.execute(sql, (correo))
    result = cursor.fetchone()
    if result is None:
        print("El usuario no existe")
        return
    idUsuario = result[0]
    ### revisamos que sea un número de pelicula valido
    sql = "SELECT * FROM peliculas WHERE nombre= %s"
    cursor.execute(sql, (titulopelicula))
    result = cursor.fetchone()
    if result is None:
        print("La pelicula no existe")
        return
    idPelicula = result[0]
    sql = "INSERT INTO rentar (idUsuario, idPelicula, fecha_renta, dias_de_renta, estatus) VALUES (%s, %s, %s, %s, %s)"
    cursor.execute(sql, (idUsuario, idPelicula, fecha_renta, dias_de_renta, estatus))
    db.commit()

### Funcion que añade datos a la base de datos 
def add_stuff ():
    add_user("Ballister", "Boldheart", "Sinbrazo", "espada", "ingenieria@gmail.com")
    add_user("Reina", "Redheart", "Martinez", "Rosas")
    add_user("Rey", "de rosa", "blackheart", "naipe", "ayelrey@gmail.com")
    add_user("Alicia", "Darling", "Perez", "4521222555", "Maravilla@elsombreo.com")
    add_movie("Nimona",98, 20, "Animacion")
    add_movie("El Rey Leon", 120, 10, "Animacion")
    add_movie("Alicia en el pais de las maravillas", 100, 15, "Animacion")
    add_movie("Pato y yo",60,4,"Animacion")
    add_rent("ingenieria@gmail.com", "Nimona", "2024-02-20")
    add_rent("ayelrey@gmail.com", "El Rey Leon", "2024-01-24")
    add_rent("Maravilla@elsombreo.com", "Alicia en el pais de las maravillas", "2023-10-21")
    add_rent("ingenieria@gmail.com", "Pato y yo", "2024-02-25")
    add_rent("ingenieria@gmail.com", "Nimona", "2024-02-25")
    add_rent("ingenieria@gmail.com", "El Rey Leon", "2024-02-25")
    add_rent("Maravilla@elsombreo.com", "Nimona", "2023-02-25")

## Función que filtre a la tabla de usuarios segun si una cadena aparece en el apellido paterno, materno o nombre.
def filter_user_by_last_name (cadena):
    cadena = "%"+cadena+"%"
    sql = "SELECT * FROM usuarios WHERE apPat LIKE %s OR apMat LIKE %s"
    cursor.execute(sql, (cadena, cadena))
    result = cursor.fetchall()
    return result 

def update_movie_genre(nomPelicula, genero):
    sql = "SELECT * FROM peliculas WHERE nombre = %s"
    cursor.execute(sql, (nomPelicula))
    result = cursor.fetchone()
    if result is None:
        print("La pelicula no existe")
        return
    nombrePelicula = result[1]
    sql = "UPDATE peliculas SET genero = %s WHERE nombre = %s"
    cursor.execute(sql, (genero, nombrePelicula))
    db.commit()

def eliminate_old_rentals():
    sql = "SELECT * FROM rentar"
    cursor.execute(sql)
    result = cursor.fetchall()
    for renta in result:
        fecha_renta = renta[3]
        if (datetime.now() - fecha_renta).days > 3:
            sql = "DELETE FROM rentar WHERE idRentar = %s"
            cursor.execute(sql, (renta[0]))
            db.commit()

if __name__ == "__main__":
    add_stuff()
    print(filter_user_by_last_name("heart"))
    update_movie_genre("Nimona", "Fantasia")
    eliminate_old_rentals()
    db.close()

