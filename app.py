from flask import Flask, render_template

app = Flask(__name__)

@app.route('/index')
def index():
    titulo = "Pagina de inicio"
    listado = ['Python', 'Flask', 'Jinja2', 'HTML', 'CSS']
    return render_template ("index.html", titulo=titulo, listado=listado)

@app.route('/calculos')
def about():
    return render_template('calculos.html')

@app.route('/distancia')
def distancia():
    return render_template('distancia.html')

@app.route('/user/<string:user>')
def user(user):
    return f"Hello, {user}"

@app.route("/numero/<int:num>")
def func(num):
    return f"El numero es:{num}"

@app.route("/suma/<int:num1>/<int:num2>")
def suma(num1, num2):
    return f"La suma es: {num1 + num2}"

app.route("/iser/<int:id>/<string:username>")
def username(id,username):
    return f"ID: {id} nombre: {username}"

@app.route("/suma/<float:n1>/<float:n2>")
def func1(n1,n2):
    return f"La suma es: {n1 + n2}"

@app.route("/default/")
@app.route("/default/<string:dft>")
def func2(dft ="sss"):
    return "El valor de dft es: " + dft

@app.route("/prueba")
def func4():
    return'''

<html>
<head>
    <title>Prueba</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.8/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-sRIl4kxILFvY47J16cr9ZwB07vP4J8+LH7qKQnuqkuIAvNWLzeN8tE5YBujZqJLB" crossorigin="anonymous">
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.8/dist/js/bootstrap.bundle.min.js" integrity="sha384-FKyoEForCGlyvwx9Hj09JcYn3nv7wiPVlz7YYwJrWVcXK/BmnVDxM+D2scQbITxI" crossorigin="anonymous"></script>

</head>
<body>
    <h1>Hola esta es una pagina de prueba</h1>
    <p>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Officia facili
        s velit praesentium! Voluptatem eos, repellat, minima unde nulla aperiam 
        architecto perspiciatis facere sit quidem ex eaque laudantium quae consequatur in.</p>
</body>
</html>

'''

if __name__ == '__main__':
    app.run(debug=True)