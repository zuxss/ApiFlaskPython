from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from utils import hash_password, verify_password, validar_datos

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Usuario
class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    usuario = db.Column(db.String(80), unique=True, nullable=False)
    contraseña = db.Column(db.String(200), nullable=False)

with app.app_context():
    db.create_all()

# Registro
@app.route('/registro', methods=['POST'])
def registro():
    datos = request.get_json()
    if not validar_datos(datos):
        return jsonify({"mensaje": "Datos inválidos"}), 400

    usuario = datos["usuario"]
    contraseña = datos["contraseña"]

    if Usuario.query.filter_by(usuario=usuario).first():
        return jsonify({"mensaje": "El Usuario ya existe"}), 400

    nuevo = Usuario(usuario=usuario, contraseña=hash_password(contraseña))
    db.session.add(nuevo)
    db.session.commit()
    return jsonify({"mensaje": "Usuario registrado"}), 201

# Login
@app.route('/login', methods=['POST'])
def login():
    datos = request.get_json()
    if not validar_datos(datos):
        return jsonify({"mensaje": "Datos inválidos"}), 400

    usuario = datos["usuario"]
    contraseña = datos["contraseña"]

    user = Usuario.query.filter_by(usuario=usuario).first()
    if not user or not verify_password(user.contraseña, contraseña):
        return jsonify({"mensaje": "Credenciales Incorrectass"}), 401

    return jsonify({"mensaje": f"Bienvenido {usuario}"}), 200

# Tareas
@app.route('/tareas', methods=['GET'])
def tareas():
    return '''
    <html>
        <h1>Bienvenido al sistema de tareas</h1>
        <p>Todo para gestionar tus tareas.</p>
    </html>
    '''

if __name__ == '__main__':
    app.run(debug=True)
    