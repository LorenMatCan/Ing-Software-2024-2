from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from datetime import datetime
from alchemyClasses import db
from alchemyClasses.Usuario import Usuario
from alchemyClasses.Pelicula import Pelicula

class Renta(db.Model):
    __tablename__ = 'rentar'
    idRentar = Column(Integer, primary_key=True, autoincrement=True)
    idUsuario = Column(Integer, db.ForeignKey(Usuario.idUsuario))
    idPelicula = Column(Integer, db.ForeignKey(Pelicula.idPelicula))
    fecha_Renta = Column(DateTime)
    dias_de_Renta = Column(Integer, default=5)
    estatus = Column(Integer, default=0)

    
    
    
    def __init__(self, idUsuario, idPelicula, fechaRenta, diasDeRenta=5, estatus=0):
        self.idUsuario = idUsuario
        self.idPelicula = idPelicula
        self.fecha_Renta = fechaRenta
        self.dias_de_Renta = diasDeRenta
        self.estatus = estatus

    def __str__(self):
        return f"{self.idRentar} Usuario: {self.idUsuario} Pelicula: {self.idPelicula} Fecha Renta: {self.fecha_Renta} Dias: {self.dias_de_Renta} Estatus: {self.estatus}"