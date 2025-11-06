from flask import Flask, jsonify
from flask_mysqldb import MySQL
from flask_cors import CORS
from config import config

app = Flask(__name__)
CORS(app)

conexion = MySQL(app)

if __name__ == '__main__':
    app.run(debug=True)
