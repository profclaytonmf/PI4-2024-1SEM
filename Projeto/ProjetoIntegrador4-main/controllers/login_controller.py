from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_user
from models import User

login_blueprint = Blueprint('login', __name__)

@login_blueprint.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user_id = request.form['user_id']
        password = request.form['password']
        user = User.query.filter_by(id=user_id, password=password).first()
        if user:
            login_user(user)
            if user.tipo == 'educando':
                return redirect(url_for('educando.home'))
            # condições aqui para outros tipos de usuários
        else:
            return 'Usuário ou senha inválidos'
    return render_template('login.html')