from flask import Flask, jsonify, request
from flask_mysqldb import MySQL
from flask_cors import CORS
from config import config

app = Flask(__name__)
app.config.from_object(config['development'])

CORS(app, resources={
    r"/*": {
        "origins": ["http://localhost:4200"],
        "methods": ["GET", "POST", "PUT", "DELETE", "OPTIONS"],
        "allow_headers": ["Content-Type"]
    }
})

conexion = MySQL(app)


@app.route('/alumnos', methods=['GET'])
def listar_alumnos():
    try:
        cursor = conexion.connection.cursor()
        cursor.execute(
            "SELECT matricula, nombre, apaterno, amaterno, correo FROM alumnos"
        )
        datos = cursor.fetchall()

        alumnos = []
        for fila in datos:
            alumnos.append({
                "matricula": fila[0],
                "nombre":   fila[1],
                "apaterno": fila[2],
                "amaterno": fila[3],
                "correo":   fila[4]
            })

        return jsonify(alumnos), 200

    except Exception as ex:
        return jsonify({"mensaje": "Error", "error": str(ex)}), 500


@app.route('/alumnos/<int:matricula>', methods=['GET'])
def leer_alumno(matricula):
    try:
        cursor = conexion.connection.cursor()
        cursor.execute(
            """
            SELECT matricula, nombre, apaterno, amaterno, correo
            FROM alumnos
            WHERE matricula = %s
            """,
            (matricula,)
        )
        fila = cursor.fetchone()

        if fila is None:
            return jsonify({"mensaje": "Alumno no encontrado"}), 404

        alumno = {
            "matricula": fila[0],
            "nombre":   fila[1],
            "apaterno": fila[2],
            "amaterno": fila[3],
            "correo":   fila[4]
        }

        return jsonify(alumno), 200

    except Exception as ex:
        return jsonify({"mensaje": "Error", "error": str(ex)}), 500


@app.route('/alumnos', methods=['POST'])
def crear_alumno():
    try:
        data = request.json

        cursor = conexion.connection.cursor()
        sql = """
            INSERT INTO alumnos (matricula, nombre, apaterno, amaterno, correo)
            VALUES (%s, %s, %s, %s, %s)
        """
        cursor.execute(sql, (
            data['matricula'],
            data['nombre'],
            data['apaterno'],
            data['amaterno'],
            data['correo']
        ))
        conexion.connection.commit()

        return jsonify({"mensaje": "Alumno creado"}), 201

    except Exception as ex:
        conexion.connection.rollback()
        return jsonify({"mensaje": "Error", "error": str(ex)}), 500


@app.route('/alumnos/<int:matricula>', methods=['PUT'])
def actualizar_alumno(matricula):
    try:
        data = request.json

        cursor = conexion.connection.cursor()
        sql = """
            UPDATE alumnos
            SET nombre = %s,
                apaterno = %s,
                amaterno = %s,
                correo = %s
            WHERE matricula = %s
        """
        cursor.execute(sql, (
            data['nombre'],
            data['apaterno'],
            data['amaterno'],
            data['correo'],
            matricula
        ))
        conexion.connection.commit()

        return jsonify({"mensaje": "Alumno actualizado"}), 200

    except Exception as ex:
        conexion.connection.rollback()
        return jsonify({"mensaje": "Error", "error": str(ex)}), 500


@app.route('/alumnos/<int:matricula>', methods=['DELETE'])
def eliminar_alumno(matricula):
    try:
        cursor = conexion.connection.cursor()
        cursor.execute(
            "DELETE FROM alumnos WHERE matricula = %s",
            (matricula,)
        )
        conexion.connection.commit()

        return jsonify({"mensaje": "Alumno eliminado"}), 200

    except Exception as ex:
        conexion.connection.rollback()
        print("ERROR EN crear_alumno:", ex)   
        return jsonify({"mensaje": "Error", "error": str(ex)}), 500



def pagina_no_encontrada(error):
    return "<h1>La página que intentas buscar no existe...</h1>", 404


if __name__ == '__main__':
    app.register_error_handler(404, pagina_no_encontrada)
    app.run(host='127.0.0.1', port=5001, debug=True)

