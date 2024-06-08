from flask import Blueprint, render_template, request

educador_blueprint = Blueprint('educador', __name__)

@educador_blueprint.route('/home')
def home():
    return render_template('EducadorHome.html')

@educador_blueprint.route('/EducadorCondTrab')
def EducadorCondTrab():
    return render_template('formsEducadoresCondicaoTrab.html')

@educador_blueprint.route('/Educador2/submit_form7', methods=['POST'])
def submit_form7():
    from app import app, mysql
    answer37 = request.form.get('answer37')
    answer38 = request.form.get('answer38')
    answer39 = request.form.get('answer39')
    answer40 = request.form.get('answer40')

    cur = mysql.connection.cursor()
    cur.execute("INSERT INTO form_educando(Q37, Q38, Q39, Q40) VALUES (%s, %s, %s, %s)", (answer37, answer38, answer39, answer40))
    mysql.connection.commit()
    cur.close()

    return 'Sucesso!'

@educador_blueprint.route('/EducadorEnsino')
def EducadorEnsino():
    return render_template('formsEducadoresQualidadeEdu.html')

@educador_blueprint.route('/Educador6/submit_form11', methods=['POST'])
def submit_form11():
    from app import app, mysql
    
    answer41 = request.form.get('answer41')
    answer42 = request.form.get('answer42')
    answer43 = request.form.get('answer43')
    answer44 = request.form.get('answer44')
    answer45 = request.form.get('answer45')
    answer46 = request.form.get('answer46')
    answer47 = request.form.get('answer47')
    answer48 = request.form.get('answer48')
    answer49 = request.form.get('answer49')
    answer50 = request.form.get('answer50')
    answer51 = request.form.get('answer51')
    answer52 = request.form.get('answer52')
    answer53 = request.form.get('answer53')
    answer54 = request.form.get('answer54')
    answer55 = request.form.get('answer55')

    cur = mysql.connection.cursor()
    cur.execute("INSERT INTO form_educando(Q41, Q42, Q43, Q44, Q45, Q46, Q47, Q48, Q49, Q50, Q51, Q52, Q53, Q54, Q55) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
                (answer41, answer42, answer43, answer44, answer45, answer46, answer47, answer48, answer49, answer50, answer51, answer52, answer53, answer54, answer55))
    mysql.connection.commit()
    cur.close()

    return 'Sucesso!'


@educador_blueprint.route('/EducadorClima')
def EducadorClima():
    return render_template('formsEducadoresClimaEscolar.html')


@educador_blueprint.route('/Educador1/submit_form6', methods=['POST'])
def submit_form6():
    from app import app, mysql
    answer56 = request.form.get('answer56')
    answer57 = request.form.get('answer57')
    answer58 = request.form.get('answer58')
    answer59 = request.form.get('answer59')

    cur = mysql.connection.cursor()
    cur.execute("INSERT INTO form_educando(Q56, Q57, Q58, Q59) VALUES (%s, %s, %s, %s)", (answer56, answer57, answer58, answer59))
    mysql.connection.commit()
    cur.close()

    return 'Sucesso!'

@educador_blueprint.route('/EducadorInfra')
def EducadorInfra():
    return render_template('formsEducadoresInfra.html')

@educador_blueprint.route('/Educador4/submit_form9', methods=['POST'])
def submit_form9():
    from app import app, mysql
    
    answer33 = request.form.get('answer33')
    answer34 = request.form.get('answer34')
    answer35 = request.form.get('answer35')
    answer36 = request.form.get('answer36')

    cur = mysql.connection.cursor()
    cur.execute("INSERT INTO form_educando(Q33, Q34, Q35, Q36) VALUES (%s, %s, %s, %s)", (answer33, answer34, answer35, answer36))
    mysql.connection.commit()
    cur.close()

    return 'Sucesso!'

@educador_blueprint.route('/EducadorGestao')
def EducadorGestao():
    return render_template('formsEducadoresGestao.html')

@educador_blueprint.route('/Educador3/submit_form8', methods=['POST'])
def submit_form8():
    from app import app, mysql
    
    answer76 = request.form.get('answer76')
    answer77 = request.form.get('answer77')
    answer78 = request.form.get('answer78')
    answer79 = request.form.get('answer79')

    cur = mysql.connection.cursor()
    cur.execute("INSERT INTO form_educando(Q76, Q77, Q78, Q79) VALUES (%s, %s, %s, %s)", (answer76, answer77, answer78, answer79))
    mysql.connection.commit()
    cur.close()

    return 'Sucesso!'


@educador_blueprint.route('/EducadorParticipacao')
def EducadorParticipacao():
    return render_template('formsEducadoresParticipacao.html')

@educador_blueprint.route('/Educador5/submit_form10', methods=['POST'])
def submit_form10():
    from app import app, mysql
    
    answer60 = request.form.get('answer60')
    answer61 = request.form.get('answer61')
    answer62 = request.form.get('answer62')
    answer63 = request.form.get('answer63')

    cur = mysql.connection.cursor()
    cur.execute("INSERT INTO form_educando(Q60, Q61, Q62, Q63) VALUES (%s, %s, %s, %s)", (answer60, answer61, answer62, answer63))
    mysql.connection.commit()
    cur.close()

    return 'Sucesso!'

@educador_blueprint.route('/FrequenciaEnviar')
def FrequenciaEnviar():
    return render_template('notasFrequenciaEnviar.html')