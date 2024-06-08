from flask import Blueprint, render_template, request
from app import mysql

educando_blueprint = Blueprint('educando', __name__)

@educando_blueprint.route('/home')
def home():
    return render_template('home.html')

@educando_blueprint.route('/dadosEducando')
def dadosEducando():  
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT (IFNULL(Q1, 0) + IFNULL(Q2, 0) + IFNULL(Q3, 0) + IFNULL(Q4, 0) + IFNULL(Q5, 0) + IFNULL(Q6, 0) + IFNULL(Q7, 0) + IFNULL(Q8, 0) + IFNULL(Q9, 0) + IFNULL(Q10, 0)) / 10 as media FROM form_educando")
    medias = cursor.fetchall()
    if medias:
        media_autonomia = sum(media[0] for media in medias if media[0] is not None) / len(medias)
    else:
        media_autonomia = 0
    return render_template('dadosEducando.html', media_autonomia=media_autonomia)

@educando_blueprint.route('/AlunosAutonomia')
def AlunosAutonomia():
    return render_template('formsAlunosAutonomia.html')

@educando_blueprint.route('/Aluno1/submit_form', methods=['POST'])
def submit_form1():
    from app import app, mysql
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
    cur.execute("INSERT INTO form_educando(Q1, Q2, Q3, Q4, Q5, Q6, Q7, Q8, Q9, Q10) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", (answer1, answer2, answer3, answer4, answer5, answer6, answer7, answer8, answer9, answer10))
    mysql.connection.commit()
    cur.close()

    return 'Sucesso!'

@educando_blueprint.route('/AlunosEnsino')
def AlunosEnsino():
    return render_template('formsAlunosQualidadeEnsino.html')

@educando_blueprint.route('/Aluno5/submit_form5', methods=['POST'])
def submit_form5():
    from app import app, mysql
    answer17 = request.form.get('answer17')
    answer18 = request.form.get('answer18')
    answer19 = request.form.get('answer19')
    answer20 = request.form.get('answer20')
    answer21 = request.form.get('answer21')
    answer22 = request.form.get('answer22')
    answer23 = request.form.get('answer23')
    answer24 = request.form.get('answer24')

    cur = mysql.connection.cursor()
    cur.execute("INSERT INTO form_educando(Q17, Q18, Q19, Q20, Q21, Q22, Q23, Q24) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)", (answer17, answer18, answer19, answer20, answer21, answer22, answer23, answer24))
    mysql.connection.commit()
    cur.close()

    return 'Sucesso!'

@educando_blueprint.route('/AlunosClima')
def AlunosClima():
    return render_template('formsAlunosClimaEscolar.html')

@educando_blueprint.route('/Aluno2/submit_form2', methods=['POST'])
def submit_form2():
    from app import app, mysql
    answer11 = request.form.get('answer11')
    answer12 = request.form.get('answer12')
    answer13 = request.form.get('answer13')
    answer14 = request.form.get('answer14')
    answer15 = request.form.get('answer15')
    answer16 = request.form.get('answer16')

    cur = mysql.connection.cursor()
    cur.execute("INSERT INTO form_educando(Q11, Q12, Q13, Q14, Q15, Q16) VALUES (%s, %s, %s, %s, %s, %s)", (answer11, answer12, answer13, answer14, answer15, answer16))
    mysql.connection.commit()
    cur.close()

    return 'Sucesso!'

@educando_blueprint.route('/AlunosInfra')
def AlunosInfra():
    return render_template('formsAlunosInfraestrutura.html')

@educando_blueprint.route('/Aluno4/submit_form4', methods=['POST'])
def submit_form4():
    from app import app, mysql
    answer25 = request.form.get('answer25')
    answer26 = request.form.get('answer26')
    answer27 = request.form.get('answer27')
    answer28 = request.form.get('answer28')

    cur = mysql.connection.cursor()
    cur.execute("INSERT INTO form_educando(Q25, Q26, Q27, Q28) VALUES (%s, %s, %s, %s)", (answer25, answer26, answer27, answer28))
    mysql.connection.commit()
    cur.close()

    return 'Sucesso!'

@educando_blueprint.route('/AlunosGestao')
def AlunosGestao():
    return render_template('formsAlunosGestao.html')

@educando_blueprint.route('/Aluno3/submit_form3', methods=['POST'])
def submit_form3():
    from app import app, mysql
    answer29 = request.form.get('answer29')
    answer30 = request.form.get('answer30')
    answer31 = request.form.get('answer31')
    answer32 = request.form.get('answer32')

    cur = mysql.connection.cursor()
    cur.execute("INSERT INTO form_educando(Q29, Q30, Q31, Q32) VALUES (%s, %s, %s, %s)", (answer29, answer30, answer31, answer32))
    mysql.connection.commit()
    cur.close()

    return 'Sucesso!'

@educando_blueprint.route('/FrequenciaVisualizar')
def FrequenciaVisualizar():
    return render_template('notasFrequenciaVisualizar.html')



  