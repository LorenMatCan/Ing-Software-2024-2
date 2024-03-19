from flask import Blueprint, render_template, url_for, redirect

index_controller = Blueprint('index_controller', __name__, template_folder='templates')

@index_controller.route('/')
def index():
    return render_template('index.html')

@index_controller.route('/peliculas')
def peliculas():
    return render_template('peliculas.html')

@index_controller.route('/rentas')
def rentas():
    return render_template('rentas.html')

@index_controller.route('/usuarios')
def usuarios():
    return render_template('usuarios.html')
