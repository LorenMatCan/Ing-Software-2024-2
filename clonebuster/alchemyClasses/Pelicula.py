from sqlalchemy import Column, Integer, String

from alchemyClasses import db

class Pelicula(db.Model):
    __tablename__ = 'peliculas'
    idPelicula = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(200))
    genero = Column(String(45), default=None)
    duracion = Column(Integer, default=None)
    inventario = Column(Integer, default=1)
    
    
    def __init__(self, nombre, genero=None, duracion= 0, inventario=1):
        self.nombre = nombre
        self.genero = genero
        self.duracion = duracion
        self.inventario = inventario

    def __str__(self):
        return f"{self.idPelicula} Pelicula: {self.nombre} Genero: {self.genero} Duracion: {self.duracion} Inventario: {self.inventario}"