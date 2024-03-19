from sqlalchemy import Column, Integer, String
import random
from alchemyClasses import db


class Usuario(db.Model):
    __tablename__ = 'usuarios'
    idUsuario = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(45))
    apPat = Column(String(45))
    apMat = Column(String(45), nullable=True)
    password = Column(String(64))
    email = Column(String(500), unique=True)
    profilePicture = Column(db.LargeBinary)
    superUser = Column(Integer, nullable=True)
    
    
    def __init__(self, nombre, apPat, email, password, apMat=None, profilePicture=None, superUser=None):
        self.nombre = nombre
        self.apPat = apPat
        self.apMat = apMat
        self.email = email
        self.password = password
        self.profilePicture = profilePicture
        self.superUser = superUser
        
    def __str__(self):
        return f"{self.idUsuario} Usuario: {self.nombre} {self.apPat} {self.apMat}  email: {self.email}  contraseña {self.password} foto {self.profilePicture} {self.superUser}"
