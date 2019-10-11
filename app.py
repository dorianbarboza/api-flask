from flask import Flask
from flask_restful import Api

from Usuario.crear import NuevoUsuario

AppInstance = Flask(__name__)
ApiInstance = Api(AppInstance)

@AppInstance.route('/', methods = ['GET'])
def main():
    return 'Servidor activado'

@AppInstance.errorhandler(404)
def not_found(error):
    return 'Recurso no encontrado'

ApiInstance.add_resource(NuevoUsuario, '/api/v1/usuario/nuevo/')

if __name__ == '__main__':
    AppInstance.run(debug = True, port = 8080, host = '127.0.0.1')
