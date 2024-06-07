from flask import Blueprint, render_template

educando_blueprint = Blueprint('educando', __name__)

@educando_blueprint.route('/home')
def home():
    return render_template('home.html')

@educando_blueprint.route('/AlunosAutonomia')
def AlunosAutonomia():
    return render_template('formsAlunosAutonomia.html')

@educando_blueprint.route('/AlunosEnsino')
def AlunosEnsino():
    return render_template('formsAlunosQualidadeEnsino.html')

@educando_blueprint.route('/AlunosClima')
def AlunosClima():
    return render_template('formsAlunosClimaEscolar.html')

@educando_blueprint.route('/AlunosInfra')
def AlunosInfra():
    return render_template('formsAlunosInfraestrutura.html')

@educando_blueprint.route('/AlunosGestao')
def AlunosGestao():
    return render_template('formsAlunosGestao.html')

@educando_blueprint.route('/FrequenciaEnviar')
def FrequenciaEnviar():
    return render_template('notasFrequenciaEnviar.html')