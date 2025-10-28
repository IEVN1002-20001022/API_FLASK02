from wtforms import Form, StringField, EmailField, IntegerField, validators

class UserForm(Form):
    matricula = IntegerField("Matrícula", [
        validators.DataRequired(message='El campo es requerido')
    ])
    nombre = StringField("Nombre", [
        validators.DataRequired(message='El campo es requerido')
    ])
    apellido = StringField("Apellido", [
        validators.DataRequired(message='El campo es requerido')
    ])
    correo = EmailField("Correo", [
        validators.DataRequired(message='El campo es requerido')
    ])
