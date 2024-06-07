from flask import Blueprint, render_template
from flask import request
from flask_mysqldb import MySQL
from flask import current_app as app

educando_blueprint = Blueprint('educando', __name__)

app.config['MYSQL_USER'] = 'aline'
app.config['MYSQL_HOST'] = '127.0.0.1'
app.config['MYSQL_PORT'] = 3306
app.config['MYSQL_PASSWORD'] = 'Newell01@'
app.config['MYSQL_DB'] = 'EducaAnalytics'

mysql = MySQL(app)

@educando_blueprint.route('/home')
def home():
    return render_template('home.html')

@educando_blueprint.route('/AlunosAutonomia')
def AlunosAutonomia():
    return render_template('formsAlunosAutonomia.html')

@educando_blueprint.route('/educandoAutonomia/submit_form', methods=['POST'])
def submit_form():
    answer1 = request.form.get('answer1')
    answer2 = request.form.get('answer2')
    answer3 = request.form.get('answer3')
    answer4 = request.form.get('answer4')
    answer5 = request.form.get('answer5')
    answer6 = request.form.get('answer6')
    answer7 = request.form.get('answer7')
    answer8 = request.form.get('answer8')
    answer9 = request.form.get('answer9')
    answer10 = request.form.get('answer10')

    cur = mysql.connection.cursor()
    cur.execute("INSERT INTO form_educando(Q1, Q2, Q3, Q4, Q5, Q6, Q7, Q8, Q9, Q10) VALUES (%s, %s, ..., %s)", (answer1, answer2, answer3, answer4, answer5, answer6, answer7, answer8, answer9, answer10))
    mysql.connection.commit()
    cur.close()

    return 'Sucesso!'

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

@educando_blueprint.route('/FrequenciaVisualizar')
def FrequenciaVisualizar():
    return render_template('notasFrequenciaVisualizar.html')



  