from flask import Flask, request, render_template, redirect, url_for
from flask_mysqldb import MySQL
from flask_wtf import FlaskForm, RecaptchaField
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired
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

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    recaptcha = RecaptchaField()
    submit = SubmitField('Login')

@app.route('/')
def home():
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        id_usuario = form.username.data
        senha = form.password.data
        senha_hash = hashlib.sha256(senha.encode()).hexdigest()
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM tLogins WHERE ID=%s AND Senha=%s", (id, senha_hash))
        usuario = cur.fetchone()
        cur.close()
        if usuario:
            return render_template('formsAlunosQualidadeEnsino.html')  
        else:
            return 'Falha no login!'
    return render_template('login.html', form=form)

@app.route('/success')
def success():
    return 'Deu certo!'

if __name__ == '__main__':
    app.run(debug=True)