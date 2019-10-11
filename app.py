from flask import Flask

AppInstance = Flask(__name__)

@AppInstance.route('/', methods = ['GET'])
def main():
    return 'Servidor activado'

@AppInstance.errorhandler(404)
def not_found(error):
    return 'Recurso no encontrado'

if __name__ == '__main__':
    AppInstance.run(debug = False, port = 5000)
