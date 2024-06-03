from flask import Blueprint, render_template

educando_blueprint = Blueprint('educando', __name__)

@educando_blueprint.route('/home')
def home():
    return render_template('home.html')

@educando_blueprint.route('/AlunoAutonomia')
def AlunoAutonomia():
    return render_template('formsAlunosAutonomia.html')

@educando_blueprint.route('/AlunoEnsino')
def AlunoEnsino():
    return render_template('formsAlunosQualidadeEnsino.html')

@educando_blueprint.route('/AlunoClima')
def AlunoClima():
    return render_template('formsAlunosClimaEscolar.html')

@educando_blueprint.route('/AlunoInfra')
def AlunosInfra():
    return render_template('formsAlunosInfraestrutura.html')

@educando_blueprint.route('/AlunoGestao')
def AlunosGestao():
    return render_template('formsAlunosGestao.html')

@educando_blueprint.route('/FrequenciaVisualizar')
def FrequenciaVisualizar():
    return render_template('notasFrequenciaVisualizar.html')