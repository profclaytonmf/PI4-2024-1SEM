from flask import Flask
from controllers.educando_controller import educando_blueprint
from controllers.educador_controller import educador_blueprint
# importar outros controladores

app = Flask(__name__)
app.register_blueprint(educando_blueprint, url_prefix='/educando')
app.register_blueprint(educador_blueprint, url_prefix='/educador')
# registrar outros controladores

if __name__ == '__main__':
    app.run(debug=True)