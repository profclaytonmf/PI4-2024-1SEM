from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_user
from models import User
import hashlib

login_blueprint = Blueprint('login', __name__)

@login_blueprint.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user_id = request.form['user_id']
        password = hashlib.sha256(request.form['password'].encode()).hexdigest()  # Hash da senha
        user = User.query.filter_by(id=user_id, password=password).first()  # Comparação com a senha hash
        if user:
            login_user(user)
            if user.tipo == 'Educando':  # Alterado para 'Educando'
                return redirect(url_for('educando.home'))
            elif user.tipo == 'Educador':  # Alterado para 'Educador'
                return redirect(url_for('educador.home'))
            elif user.tipo == 'Gestor':  # Alterado para 'Gestor'
                return redirect(url_for('gestor.home'))
            elif user.tipo == 'Funcionario':  # Alterado para 'Funcionario'
                return redirect(url_for('funcionario.home'))
            else:
                return 'Tipo de usuário não reconhecido'
        else:
            return 'Usuário ou senha inválidos'
    else:
        return render_template('login.html')