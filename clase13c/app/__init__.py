from flask import Flask, flash, url_for,redirect,render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///estudiantes.sqlite3'
app.config['SECRET_KEY'] = 'uippc3'

db = SQLAlchemy(app)
class Estudiantes(db.Model):
    id = db.Column('id', db.integer, primary_key = True)
    nombre = db.Column(db.String(100))
    ciudad = db.Column(db.String(50))
    direccion = db.Column(db.String(200))
    pin = db.Column(db.String(10))
    def __init__(self, nombre, ciudad, direccion, pin):
        self.nombre = nombre
        self.ciudad = ciudad
        self.direccion = direccion
        self.pin = pin

@app.route('/')
def mostrar_todo():
    return render_template('mostrar_todo.html', estudiantes=estudiantes.query.a)

@app.route('/nuevo', methods= ['GET','POST'])
def nuevo():