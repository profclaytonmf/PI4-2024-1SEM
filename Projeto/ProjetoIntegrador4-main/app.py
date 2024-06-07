from flask import Flask, redirect, url_for, request
from flask_login import LoginManager, UserMixin, login_user
from flask_mysqldb import MySQL
from controllers.educando_controller import educando_blueprint
from controllers.educador_controller import educador_blueprint
from controllers.gestor_controller import gestor_blueprint
from controllers.funcionario_controller import funcionario_blueprint
from controllers.login_controller import login_blueprint
import hashlib

app = Flask(__name__)
app.config['SECRET_KEY'] = '6LelIO0pAAAAADNdXiI48Ux0Qg0FI6ihzjiJwg6z'
app.config['MYSQL_USER'] = 'aline'
app.config['MYSQL_HOST'] = '127.0.0.1'
app.config['MYSQL_PORT'] = 3306
app.config['MYSQL_PASSWORD'] = 'Newell01@'
app.config['MYSQL_DB'] = 'EducaAnalytics'
app.config['RECAPTCHA_PUBLIC_KEY'] = '6LelIO0pAAAAANRPlTGQtlT5S_ytbg2zX8Sh_lir'

mysql = MySQL(app)

# Inicializa o Login
login_manager = LoginManager()
login_manager.init_app(app)

class User(UserMixin):
    def __init__(self, id, senha, tipo, active=True):
        self.id = id
        self.senha = senha
        self.tipo = tipo
        self.active = active

    @property
    def is_active(self):
        return self.active

@login_manager.user_loader
def load_user(user_id):
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM usuarios WHERE ID = %s', [user_id])
    usuario = cur.fetchone()
    if usuario:
        return User(id=usuario[0], senha=usuario[5], tipo=usuario[4])  # Ajustado para senha=usuario[5] e tipo=usuario[4]
    return None

@app.route('/login/login', methods=['POST'])
def login():
    user_id = request.form['user_id']
    password = hashlib.sha256(request.form['password'].encode()).hexdigest()
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM usuarios WHERE ID = %s AND Senha = %s', (user_id, password))
    usuario = cur.fetchone()
    if usuario:
        user = User(id=usuario[0], senha=usuario[5], tipo=usuario[4], active=True)  # Ajustado para senha=usuario[5] e tipo=usuario[4]
        login_user(user)
        if user.tipo == 'Educando':
            return redirect(url_for('educando.home'))
        elif user.tipo == 'Educador':
            return redirect(url_for('educador.home'))
        elif user.tipo == 'Gestor':
            return redirect(url_for('gestor.home'))
        elif user.tipo == 'Funcionario':
            return redirect(url_for('funcionario.home'))
        else:
            return 'Tipo de usuário não reconhecido'
    else:
        return 'Usuário ou senha inválidos'  
    
app.register_blueprint(login_blueprint, url_prefix='/login')
app.register_blueprint(educando_blueprint, url_prefix='/educando')
app.register_blueprint(educador_blueprint, url_prefix='/educador')
app.register_blueprint(gestor_blueprint, url_prefix='/gestor')
app.register_blueprint(funcionario_blueprint, url_prefix='/funcionario')

@app.route('/')
def default():
    return redirect(url_for('login.login'))

if __name__ == '__main__':
    app.run(debug=True)