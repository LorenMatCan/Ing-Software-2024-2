from alchemyClasses import db
from alchemyClasses.Renta import Renta
import datetime 

def actualiza_fecha_renta(id, nuevo_nombre):
    renta = Renta.query.filter(Renta.idRentar == id).first()
    if renta is None:
        print("No se encontro la renta")
        return
    nuevaFecha = datetime.datetime.strptime(nuevo_nombre, '%Y-%m-%d')
    renta.fecha_Renta  = nuevaFecha
    db.session.commit()
    print("Renta actualizado con éxito")

def eliminar_renta_usuario(idUsuario):
    for renta in Renta.query.filter(Renta.idUsuario == idUsuario).all():
        db.session.delete(renta)
    db.session.commit()
    print("Renta eliminada con éxito")

def eliminar_renta_pelicula(idPelicula):
    for renta in Renta.query.filter(Renta.idPelicula == idPelicula).all():
        db.session.delete(renta)
    db.session.commit()
    print("Renta eliminada con éxito")

def eliminar_renta(id):
    renta = Renta.query.filter(Renta.idRentar == id).first()
    if renta is None:
        print("No se encontro la renta")
        return
    db.session.delete(renta)
    db.session.commit()
    print("Renta eliminada con éxito")

def añadir_renta( idUsuario, idPelicula, fechaRenta, diasRenta=5, estatus=0):
    renta = Renta(idUsuario, idPelicula, fechaRenta, diasRenta)
    db.session.add(renta)
    db.session.commit()
    print("Renta añadida con éxito")