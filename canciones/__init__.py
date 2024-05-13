from flask import Flask,render_template

app = Flask(__name__)

with app.app_context():
    from . import db
    db.init_app(app)


@app.route('/')
def hello():
    return 'Hello, World!'


@app.route('/cancion')
def cancion():
    base_datos = db.get_db()
    consulta = """SELECT name FROM tracks"""

    resultado = base_datos.execute(consulta)
    lista_resultados = resultado.fetchall()
    return render_template('cancion.html', cancion=lista_resultados)

