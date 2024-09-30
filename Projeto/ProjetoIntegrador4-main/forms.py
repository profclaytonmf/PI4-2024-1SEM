from flask import Flask, request, render_template
from flask import Blueprint
from flask_mysqldb import MySQL

app = Flask(__name__)

# Configuração MySQL
app.config['MYSQL_USER'] = 'aline'  
app.config['MYSQL_HOST'] = '127.0.0.1'
app.config['MYSQL_PORT'] = 3306
app.config['MYSQL_PASSWORD'] = 'Newell01@'  
app.config['MYSQL_DB'] = 'EducaAnalytics'

mysql = MySQL(app)

forms_blueprint = Blueprint('forms', __name__)

@forms_blueprint.route('/form1')
def form1():
    return render_template('form1.html')

@forms_blueprint.route('/form2')
def form2():
    return render_template('form2.html')

if __name__ == '__main__':
    app.run(debug=True)