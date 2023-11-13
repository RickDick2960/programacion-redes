# Creando un servidor Web con Flask para proporcionar servicios
# mediante los métodos GET, PUT, DELETE, POST
# Gabriel Barrón R.

import json
import sqlite3
from flask import Flask, request, jsonify

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('crud.db')
    conn.row_factory = sqlite3.Row
    return conn

# Método GET donde busca un nombre
@app.route('/', methods=['GET'])
def query_records():
    name = request.args.get('nombre')
    registros = []
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM empleados')
    data = cursor.fetchall()
    for reg in data:
       registros.append(dict(reg))
    conn.close()
    return jsonify(json.dumps(registros))

app.run(debug=True)