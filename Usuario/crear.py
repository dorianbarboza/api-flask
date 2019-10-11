from flask_restful import Resource, request
from wtforms import Form, validators, StringField, PasswordField

class NuevoUsuarioForm(Form):
    telefono = StringField('Telefono del usuario', [validators.DataRequired()])
    password = PasswordField('Constraseña del usuario', [validators.DataRequired()])

class NuevoUsuario(Resource):
    def post(self):
        form = NuevoUsuarioForm(request.form)
        if not form.validate():
            return 'Error', 400
        return 'Satisfactorio', 200
