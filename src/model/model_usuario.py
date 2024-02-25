from alchemyClasses import db
from alchemyClasses.Usuario import Usuario

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
    db.session.delete(usuario)
    db.session.commit()
    print("Usuario eliminado con éxito")