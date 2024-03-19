from alchemyClasses import db
from alchemyClasses.Usuario import Usuario
from model.model_renta import eliminar_renta_usuario

def actualiza_nombre_usuario(id, nuevo_nombre):
    usuario = Usuario.query.filter(Usuario.idUsuario == id).first()
    if usuario is None:
        print("No se encontro el usuario")
        return
    usuario.nombre = nuevo_nombre
    db.session.commit()
    print("Usuario actualizado con éxito")

def eliminar_usuario(id):
    usuario = Usuario.query.filter(Usuario.idUsuario == id).first()
    if usuario is None:
        print("No se encontro el usuario")
        return
    eliminar_renta_usuario(id)
    db.session.delete(usuario)
    db.session.commit()
    print("Usuario eliminado con éxito")

def añadir_usuario(nombre, apPat, password,email, apMat=None):
    usuario = Usuario(nombre, apPat, email,password, apMat)
    db.session.add(usuario)
    db.session.commit()
    print("Usuario añadido con éxito")

def obtener_usuarios():
    return Usuario.query.all()