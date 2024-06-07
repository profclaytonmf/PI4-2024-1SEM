from flask import Blueprint, render_template

gestor_blueprint = Blueprint('gestor', __name__)

@gestor_blueprint.route('/home')
def home():
    return render_template('GestorHome.html')

@gestor_blueprint.route('/FrequenciaEnviar')
def FrequenciaEnviar():
    return render_template('notasFrequenciaEnviarGestor.html')