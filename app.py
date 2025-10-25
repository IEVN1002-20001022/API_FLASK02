from flask import Flask, render_template, request
import math

app = Flask(__name__)

@app.route('/index')
def index():
    titulo = "Pagina de inicio"
    listado = ['Python', 'Flask', 'Jinja2', 'HTML', 'CSS']
    return render_template("index.html", titulo=titulo, listado=listado)

@app.route('/calculos', methods=['GET', 'POST'])
def calculos():
    if request.method == 'POST':
        numero1 = float(request.form['numero1'])
        numero2 = float(request.form['numero2'])
        opcion = request.form['opcion']

        if opcion == "suma":
            res = int(numero1) + int(numero2)
        elif opcion == "resta":
            res = int(numero1) - int(numero2)
        elif opcion == "multiplicacion":
            res = int(numero1) * int(numero2)
        elif opcion == "division":
            res = int(numero1) / int(numero2)
        else:
            res = "Operación no válida"

        return render_template('calculos.html', opcion=opcion, res=res, numero1=numero1, numero2=numero2)
    return render_template('calculos.html')

@app.route('/distancia', methods=['GET', 'POST'])
def distancia():
    disRes = None
    if request.method == 'POST':
        x1 = float(request.form['x1'])
        y1 = float(request.form['y1'])
        x2 = float(request.form['x2'])
        y2 = float(request.form['y2'])

        disRes = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

    return render_template('distancia.html', disRes=disRes)

@app.route('/user/<string:user>')
def user(user):
    return f"Hello, {user}"

@app.route("/numero/<int:num>")
def func(num):
    return f"El numero es: {num}"

@app.route("/suma/<int:num1>/<int:num2>")
def suma(num1, num2):
    return f"La suma es: {num1 + num2}"

@app.route("/user/<int:id>/<string:username>")
def username(id, username):
    return f"ID: {id}, nombre: {username}"

@app.route("/suma/<float:n1>/<float:n2>")
def func1(n1, n2):
    return f"La suma es: {n1 + n2}"

@app.route("/default/")
@app.route("/default/<string:dft>")
def func2(dft="sss"):
    return "El valor de dft es: " + dft

@app.route("/prueba")
def func4():
    return '''
    <html>
    <head><title>Prueba</title></head>
    <body>
        <h1>Hola esta es una página de prueba</h1>
    </body>
    </html>
    '''

if __name__ == '__main__':
    app.run(debug=True)
