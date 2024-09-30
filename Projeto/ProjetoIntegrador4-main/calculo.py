from flask import Flask, request, render_template
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_USER'] = 'aline'  
app.config['MYSQL_HOST'] = '127.0.0.1'
app.config['MYSQL_PORT'] = 3306
app.config['MYSQL_PASSWORD'] = 'Newell01@'  
app.config['MYSQL_DB'] = 'EducaAnalytics'

mysql = MySQL(app)


@app.route('/average')
def average():
    cur = mysql.connection.cursor()

    cur.execute("SELECT Q1, Q2, Q3, Q4, Q5, Q6, Q7, Q8, Q9, Q10 FROM tformseducandos")

    rows = cur.fetchall()

    cur.close()

    sum = 0
    count = 0
    for row in rows:
        for answer in row:
            sum += answer
            count += 1

    average = sum / count if count > 0 else 0

    return 'A média das respostas é: {}'.format(average)