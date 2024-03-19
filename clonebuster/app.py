from flask import Flask, render_template, url_for, redirect
from alchemyClasses import db

from controller.indexController import index_controller
from controller.usuarioController import usuario_controller
from controller.peliculaController import pelicula_controller
from controller.rentaController import renta_controller

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://lab:Developer123!@localhost:3306/lab_ing_software'
app.config.from_mapping(
    SECRET_KEY='dev'
)

db.init_app(app)
app.register_blueprint(index_controller)
app.register_blueprint(usuario_controller)
app.register_blueprint(pelicula_controller)
app.register_blueprint(renta_controller)






if __name__ == '__main__':
    app.run(debug=True)