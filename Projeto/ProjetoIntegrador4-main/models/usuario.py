from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired
import hashlib

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')

class Usuario:
    def __init__(self, id, senha):
        self.id = id
        self.senha = senha

    def verificar_senha(self, senha):
        senha_hash = hashlib.sha256(senha.encode()).hexdigest()
        return self.senha == senha_hash