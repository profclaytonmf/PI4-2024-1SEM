from flask import Blueprint, render_template, request

funcionario_blueprint = Blueprint('funcionario', __name__)

@funcionario_blueprint.route('/home')
def home():
    return render_template('FuncionarioHome.html')

@funcionario_blueprint.route('/FuncionarioGestao')
def FuncionarioGestao():
    return render_template('formsFuncionariosGestao.html')

@funcionario_blueprint.route('/Funcionario1/submit_form12', methods=['POST'])
def submit_form12():
    from app import app, mysql
    
    answer68 = request.form.get('answer68')
    answer69 = request.form.get('answer69')
    answer70 = request.form.get('answer70')
    answer71 = request.form.get('answer71')

    cur = mysql.connection.cursor()
    cur.execute("INSERT INTO form_funcionario(Q68, Q69, Q70, Q71) VALUES (%s, %s, %s, %s)", (answer68, answer69, answer70, answer71))
    mysql.connection.commit()
    cur.close()

    return 'Sucesso!'

@funcionario_blueprint.route('/FuncionarioInfra')
def FuncionarioInfra():
    return render_template('formsFuncionarioInfraestrutura.html')


@funcionario_blueprint.route('/Funcionario2/submit_form13', methods=['POST'])
def submit_form13():
    from app import app, mysql
    
    answer72 = request.form.get('answer72')
    answer73 = request.form.get('answer73')
    answer74 = request.form.get('answer74')
    answer75 = request.form.get('answer75')

    cur = mysql.connection.cursor()
    cur.execute("INSERT INTO form_funcionario(Q72, Q73, Q74, Q75) VALUES (%s, %s, %s, %s)", (answer72, answer73, answer74, answer75))
    mysql.connection.commit()
    cur.close()

    return 'Sucesso!'

@funcionario_blueprint.route('/FuncionarioSatis')
def FuncionarioSatis():
    return render_template('formsFuncionarioSatisfacao.html')


@funcionario_blueprint.route('/Funcionario3/submit_form14', methods=['POST'])
def submit_form14():
    from app import app, mysql
    
    answer64 = request.form.get('answer64')
    answer65 = request.form.get('answer65')
    answer66 = request.form.get('answer66')
    answer67 = request.form.get('answer67')

    cur = mysql.connection.cursor()
    cur.execute("INSERT INTO form_funcionario(Q64, Q65, Q66, Q67) VALUES (%s, %s, %s, %s)", (answer64, answer65, answer66, answer67))
    mysql.connection.commit()
    cur.close()

    return 'Sucesso!'