from flask import Flask, request, render_template
from flask_mysqldb import MySQL

app = Flask(__name__)

# Configuração MySQL
app.config['MYSQL_USER'] = 'aline'  
app.config['MYSQL_HOST'] = '127.0.0.1'
app.config['MYSQL_PORT'] = 3306
app.config['MYSQL_PASSWORD'] = 'Newell01@'  
app.config['MYSQL_DB'] = 'EducaAnalytics'

mysql = MySQL(app)

@app.route('/')
def home():
    return render_template('formsAutonomiaAlunos.html')

@app.route('/submit_form', methods=['POST'])
def submit_form():
    if request.method == 'POST':

        answer1 = request.form['answer1']
        answer2 = request.form['answer2']
        answer3 = request.form['answer3']
        answer4 = request.form['answer4']
        answer5 = request.form['answer5']
        answer6 = request.form['answer6']
        answer7 = request.form['answer7']
        answer8 = request.form['answer8']
        answer9 = request.form['answer9']
        answer10 = request.form['answer10']
        
        cur = mysql.connection.cursor()


        cur.execute("INSERT INTO tformseducandos (Q1, Q2, Q3, Q4, Q5, Q6, Q7, Q8, Q9, Q10) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", 
                    (answer1, answer2, answer3, answer4, answer5, answer6, answer7, answer8, answer9, answer10))


        mysql.connection.commit()


        cur.close()

        return 'Sucesso!'
    else:
        return 'Erro na solicitação.'

if __name__ == '__main__':
    app.run(debug=True)