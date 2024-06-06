from flask import Blueprint, render_template

funcionario_blueprint = Blueprint('funcionario', __name__)

@funcionario_blueprint.route('/home')
def home():
    return render_template('FuncionarioHome.html')

@funcionario_blueprint.route('/Gestor')
def FuncionarioGestao():
    return render_template('formsFuncionariosGestao.html')

@funcionario_blueprint.route('/FuncionarioInfra')
def FuncionarioInfra():
    return render_template('formsFuncionarioInfraestrutura.html')

@funcionario_blueprint.route('/FuncionarioSatis')
def FuncionarioSatis():
    return render_template('formsFuncionarioSatisfacao.html')