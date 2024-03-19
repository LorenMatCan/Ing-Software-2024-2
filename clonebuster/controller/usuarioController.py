from flask import Blueprint, render_template, url_for, redirect, request
from model import model_usuario

usuario_controller = Blueprint('usuario_controller', __name__, template_folder='templates')

@usuario_controller.route('/crear_usuario',  methods=['GET','POST'])
def crear_usuario():
    if request.method == 'POST':
        nombre = request.form['nombre']
        apPat = request.form['apPat']
        apMat = request.form['apMat']
        password = request.form['password']
        email = request.form['email']
        model_usuario.añadir_usuario(nombre, apPat, password,email, apMat)
        return redirect(url_for('usuario_controller.ver_usuarios'))
    else:
        return render_template('usuarios/crear_usuario.html')

@usuario_controller.route('/editar_usuario',methods=['GET','POST'])
def actualizar_usuario():
    if request.method == 'POST':
        idUsuario = request.form['id']
        nombre = request.form['nombre']
        model_usuario.actualiza_nombre_usuario(idUsuario, nombre)
        return redirect(url_for('usuario_controller.ver_usuarios'))
    else:
        return render_template('usuarios/actualizar_usuario.html')

@usuario_controller.route('/eliminar_usuario',methods=['GET','POST'])
def eliminar_usuario():
    if request.method == 'POST':
        idUsuario = request.form['id']
        model_usuario.eliminar_usuario(idUsuario)
        return redirect(url_for('usuario_controller.ver_usuarios'))
    else:
        return render_template('usuarios/eliminar_usuario.html')


@usuario_controller.route('/ver_usuarios',methods=['GET','POST'])
def ver_usuarios():
    usuarios = model_usuario.obtener_usuarios()
    return render_template('usuarios/ver_usuarios.html', usuarios=usuarios)