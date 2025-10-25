import math
import forms
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/index')
def index():
    titulo =  "Pagina de Inicio"
    listado =  ['Python', 'Flask', 'Jinja2', 'HTML', 'CSS']
    return render_template('index.html', titulo=titulo, listado=listado)

@app.route('/calculos', methods=['GET','POST'])
def about():
    if request.method == 'POST':
        numero1 = request.form['numero1']
        numero2 = request.form['numero2']
        operacion = request.form['operacion']

        if operacion == 'suma':
            res = int(numero1) + int(numero2)
        if operacion == 'resta':
            res = int(numero1) - int(numero2)
        if operacion == 'multiplicacion':
            res = int(numero1) * int(numero2)
        if operacion == 'division':
            res = int(numero1) / int(numero2)

        return render_template('calculos.html', operacion=operacion, res=res, numero1=numero1, numero2=numero2)
    return render_template('calculos.html')

@app.route('/distancia', methods=['GET','POST'])
def distancia():
    if request.method == 'POST':
        numero1 = request.form['numero1']
        numero2 = request.form['numero2']
        numero3 = request.form['numero3']
        numero4 = request.form['numero4']
        operacion = request.form['operacion']

        if operacion == 'distancia':
            res = math.sqrt((int(numero2) - int(numero1))**2 + (int(numero4) - int(numero3))**2)


        return render_template('distancia.html', operacion=operacion, res=res, numero1=numero1, numero2=numero2, numero3=numero3,  numero4=numero4)
    return render_template('distancia.html')

@app.route('/Alumnos', methods=['GET','POST'])
def alumnos():
    mat=0
    nom=""
    ape=""
    email=""
    alumno_clas = forms.UserForm(request.form)
    if request.method == 'POST' and alumno_clas.validate():
        mat=alumno_clas.matricula.data
        nom=alumno_clas.nombre.data
        ape=alumno_clas.apellido.data
        email=alumno_clas.correo.data
        
    return render_template('alumnos.html', form=alumno_clas, mat=mat, nom=nom, ape=ape, email=email)

@app.route('/user/<string:user>')
def user(user):
    return f"Hello, {user}!"

@app.route('/numero/<int:num>')
def func(num):
    return f"El número es: {num}!"

@app.route('/suma/<int:num1>/<int:num2>')
def suma(num1, num2):
    return f"El suma es: {num1 + num2}"

@app.route('/user/<int:id>/<string:username>')
def username(id, username):
    return "ID: {} nombre: {}".format(id,username)

@app.route('/suma/<float:n1>/<float:n2>')
def func1(n1, n2):
    return "El suma es: {}".format(n1+n2)

@app.route('/default/')
@app.route('/default/<string:dft>')
def func2(dft="sss"):
    return "el valor de dft es:"+ dft

@app.route('/prueba')
def func4():
    return '''<!DOCTYPE html>
<html lang="en">
<head>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.8/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-sRIl4kxILFvY47J16cr9ZwB07vP4J8+LH7qKQnuqkuIAvNWLzeN8tE5YBujZqJLB" crossorigin="anonymous">
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
<h1>Hola esta es una pagina de prueba</h1>
<p>Esta es una pagina para probar el retorno</p>
    
</body>
</html>'''


if __name__ == '__main__':
    app.run(debug=True)