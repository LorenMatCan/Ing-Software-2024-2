from flask import Blueprint, render_template, url_for, redirect, request
from model import model_renta

renta_controller = Blueprint('renta_controller', __name__, template_folder='templates')

@renta_controller.route('/crear_renta',methods=['GET','POST'])
def crear_renta():
    if request.method == 'POST':
        idUsuario = request.form['idUsuario']
        idPelicula = request.form['idPelicula']
        fechaRenta = request.form['fechaRenta']
        diasRenta = request.form['diasRenta']
        model_renta.añadir_renta(idUsuario, idPelicula, fechaRenta, diasRenta)
        return redirect(url_for('renta_controller.ver_renta')) 
    else:
        return render_template('rentas/crear_renta.html')
    
@renta_controller.route('/editar_renta',methods=['GET','POST'])
def actualizar_renta():
    if request.method == 'POST':
        idRenta = request.form['id']
        fechaRenta = request.form['fecha']
        model_renta.actualiza_fecha_renta(idRenta, fechaRenta)
        return redirect(url_for('renta_controller.ver_renta'))
    else:
        return render_template('rentas/actualizar_renta.html')

@renta_controller.route('/eliminar_renta',methods=['GET','POST'])
def eliminar_renta():
    if request.method == 'POST':
        idRenta = request.form['id']
        model_renta.eliminar_renta(idRenta)
        return redirect(url_for('renta_controller.ver_renta'))
    else:
        return render_template('rentas/eliminar_renta.html')

@renta_controller.route('/ver_rentas',methods=['GET','POST'])
def ver_renta():
    rentas = model_renta.obtener_rentas()
    return render_template('rentas/ver_renta.html', rentas=rentas)
