from flask import Flask
from flask_mysqldb import MySQL

app = Flask(__name__)
app.config['MYSQL_USER'] = 'aline'
app.config['MYSQL_HOST'] = '127.0.0.1'
app.config['MYSQL_PORT'] = 3306
app.config['MYSQL_PASSWORD'] = 'Newell01@'
app.config['MYSQL_DB'] = 'EducaAnalytics'

mysql = MySQL(app)