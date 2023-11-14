# Creando un servidor Web con Flask para proporcionar servicios
# mediante los métodos GET, PUT, DELETE, POST
# Gabriel Barrón R.

import json
import sqlite3
from flask import Flask, request, jsonify

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('BaseDatos.db')
    conn.row_factory = sqlite3.Row
    return conn

# Método GET donde busca un nombre
@app.route('/', methods=['GET'])
def query_records():
    nombre = request.args.get('nombre')
    registros = []
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM empleado WHERE nombre = ?', (nombre,))
    data = cursor.fetchall()
    for reg in data:
       registros.append(dict(reg))
    conn.close()
    return jsonify(json.dumps(registros))

@app.route('/', methods=['PUT'])
def create_record():
    record = json.loads(request.data)

    conn = get_db_connection()
    cursor = conn.cursor()
    insert = 'INSERT INTO empleado(id, nombre, paterno, puesto) VALUES(?,?,?,?)'
    cursor.execute(insert, (record['id'], record['nombre'], record['paterno'], record['puesto']))
    conn.commit()
    return jsonify(record)

@app.route('/', methods=['DELETE'])
def delete_record():
    record = json.loads(request.data)
   
    conn = get_db_connection()
    cursor = conn.cursor()
    delete = 'DELETE FROM empleado WHERE id = ?'
    cursor.execute(delete, (record['id'],))
    conn.commit()
    return jsonify(record)

@app.route('/', methods=['POST'])
def update_record():
    record = json.loads(request.data)
    
    conn = get_db_connection()
    cursor = conn.cursor()
    update = 'UPDATE empleado SET puesto = ? WHERE nombre = ?'
    cursor.execute(update, (record['puesto'], record['nombre']))
    conn.commit()
    return jsonify(record)

app.run(debug=True)
