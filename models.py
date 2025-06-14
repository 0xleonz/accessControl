# to test
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Usuario(db.Model):
    __tablename__ = 'usuarios'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    es_profesor = db.Column(db.Boolean, default=False)

class Curso(db.Model):
    __tablename__ = 'cursos'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    profesor_id = db.Column(db.Integer, db.ForeignKey('usuarios.id'))

class Calificacion(db.Model):
    __tablename__ = 'calificaciones'
    id = db.Column(db.Integer, primary_key=True)
    valor = db.Column(db.Float, nullable=False)
    alumno_id = db.Column(db.Integer, db.ForeignKey('usuarios.id'))
    curso_id = db.Column(db.Integer, db.ForeignKey('cursos.id'))
