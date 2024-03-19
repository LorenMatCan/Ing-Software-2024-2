from flask import Blueprint, render_template, url_for, redirect, request
from model import model_pelicula

pelicula_controller = Blueprint('pelicula_controller', __name__, template_folder='templates')

@pelicula_controller.route('/crear_pelicula',methods=['GET','POST'])
def crear_pelicula():
    if request.method == 'POST':
        nombre = request.form['nombre']
        genero = request.form['genero']
        duracion = request.form['duracion']
        inventario = request.form['inventario']
        model_pelicula.añadir_pelicula(nombre, genero, duracion, inventario)
        return redirect(url_for('pelicula_controller.ver_pelicula'))
    else:
        return render_template('peliculas/crear_pelicula.html')

@pelicula_controller.route('/actualizar_pelicula',methods=['GET','POST'])
def actualizar_pelicula():
    if request.method == 'POST':
        idPelicula = request.form['id']
        nombre = request.form['nombre']
        model_pelicula.actualiza_nombre_pelicula(idPelicula, nombre)
        return redirect(url_for('pelicula_controller.ver_pelicula'))
    else:
        return render_template('peliculas/actualizar_pelicula.html')


@pelicula_controller.route('/eliminar_pelicula',methods=['GET','POST'])
def eliminar_pelicula():
    if request.method == 'POST':
        idPelicula = request.form['id']
        model_pelicula.eliminar_pelicula(idPelicula)
        return redirect(url_for('pelicula_controller.ver_pelicula'))
    else:
        return render_template('peliculas/eliminar_pelicula.html')

@pelicula_controller.route('/ver_peliculas',methods=['GET','POST'])
def ver_pelicula():
    peliculas = model_pelicula.obtener_peliculas()
    return render_template('peliculas/ver_pelicula.html', peliculas=peliculas)