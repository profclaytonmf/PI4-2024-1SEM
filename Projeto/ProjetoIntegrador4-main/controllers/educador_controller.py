from flask import Blueprint, render_template

educador_blueprint = Blueprint('educador', __name__)

@educador_blueprint.route('/home')
def home():
    return render_template('EducadorHome.html')

@educador_blueprint.route('/EducadorCondTrab')
def EducadorCondTrab():
    return render_template('formsEducadoresCondicaoTrab.html')

@educador_blueprint.route('/EducadorEnsino')
def EducadorEnsino():
    return render_template('formsEducadoresQualidadeEdu.html')

@educador_blueprint.route('/EducadorClima')
def EducadorClima():
    return render_template('formsEducadoresClimaEscolar.html')

@educador_blueprint.route('/EducadorInfra')
def EducadorInfra():
    return render_template('formsEducadoresInfra.html')

@educador_blueprint.route('/EducadorGestao')
def EducadorGestao():
    return render_template('formsFuncionariosGestao.html')

@educador_blueprint.route('/EducadorParticipacao')
def EducadorParticipacao():
    return render_template('formsEducadoresParticipacao.html')

@educador_blueprint.route('/FrequenciaEnviar')
def FrequenciaEnviar():
    return render_template('notasFrequenciaEnviar.html')