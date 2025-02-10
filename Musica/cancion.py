from flask import Flask, render_template
import sqlite3  

app = Flask(__name__)

@app.route('/')
def inicio():
    return render_template('inicio.html')

@app.route('/cancion')
def cancion():
    base_datos = get_db()  
    consulta = """SELECT name FROM tracks"""
    resultado = base_datos.execute(consulta)
    lista_resultados = resultado.fetchall()
    return render_template('cancion.html', cancion=lista_resultados)

def get_db():
    conn = sqlite3.connect('ruta_a_tu_base_de_datos.db') 
    conn.row_factory = sqlite3.Row  
    return conn

if __name__ == "__main__":
    app.run(debug=True)