from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')
@app.route('/pagina1')
def pagina1():
    return render_template('pagina1.html')

@app.route('/pagina2')
def pagina2():
    return render_template('pagina2.html')

@app.route('/pagina3')
def pagina3():
    return render_template('pagina3.html')

if __name__ == '__main__':
    app.run(debug=True)