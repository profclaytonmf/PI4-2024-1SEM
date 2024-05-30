from flask import Flask, request, render_template, redirect, url_for
from flask_mysqldb import MySQL
import hashlib

app = Flask(__name__)
app.config['MYSQL_USER'] = 'aline'  
app.config['MYSQL_HOST'] = '127.0.0.1'
app.config['MYSQL_PORT'] = 3306
app.config['MYSQL_PASSWORD'] = 'Newell01@'  
app.config['MYSQL_DB'] = 'EducaAnalytics'  

mysql = MySQL(app)

@app.route('/')
def home():
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        id_usuario = request.form['username']
        senha = request.form['password']
        senha_hash = hashlib.sha256(senha.encode()).hexdigest()
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM tLogins WHERE ID_Usuario=%s AND Senha=%s", (id_usuario, senha_hash))
        usuario = cur.fetchone()
        cur.close()
        if usuario:
            return render_template('formsAlunosQualidadeEnsino.html')  
        else:
            return 'Falha no login!'
    return render_template('login.html')

@app.route('/success')
def success():
    return 'Deu certo!'

if __name__ == '__main__':
    app.run(debug=True)