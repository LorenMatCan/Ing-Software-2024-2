from alchemyClasses import db
from alchemyClasses.Pelicula import Pelicula

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
    db.session.delete(pelicula)
    db.session.commit()
    print("La pelicula se ha eliminado con éxito")