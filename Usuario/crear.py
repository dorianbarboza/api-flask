from flask_restful import Resource, request
from wtforms import Form, validators, StringField, PasswordField

from util.form import check

class NuevoUsuarioForm(Form):
    telefono = StringField('Telefono del usuario', [validators.DataRequired()])
    password = PasswordField('Constraseña del usuario', [validators.DataRequired()])

class NuevoUsuario(Resource):
    @check(NuevoUsuarioForm)
    def post(self):
        form = NuevoUsuarioForm(request.form)
        return 'Creado'
