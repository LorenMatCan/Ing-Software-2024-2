from alchemyClasses import db
from alchemyClasses.Pelicula import Pelicula
from model.model_renta import eliminar_renta_pelicula

def actualiza_nombre_pelicula(id, nuevo_nombre):
    pelicula = Pelicula.query.filter(Pelicula.idPelicula == id).first()
    if pelicula is None:
        print("No se encontro la pelicula")
        return
    pelicula.nombre = nuevo_nombre
    db.session.commit()
    print("La pelicula se ha actualizado con éxito")

def eliminar_pelicula(id):
    pelicula = Pelicula.query.filter(Pelicula.idPelicula == id).first()
    if pelicula is None:
        print("No se encontro la pelicula")
        exit()
    eliminar_renta_pelicula(id)
    db.session.delete(pelicula)
    db.session.commit()
    print("La pelicula se ha eliminado con éxito")

def añadir_pelicula(nombre, genero = None, duracion = 0, inventario = 1):
    pelicula = Pelicula(nombre, genero, duracion, inventario)
    db.session.add(pelicula)
    db.session.commit()
    print("La pelicula se ha añadido con éxito")

def obtener_peliculas():
    return Pelicula.query.all()