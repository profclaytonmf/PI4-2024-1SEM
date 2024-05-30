from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('login.html')
@app.route('/indexAlunos')
def indexAlunos():
    return render_template('indexAlunos.html')
@app.route('/AlunoAutonomia')
def AlunoAutonomia():
    return render_template('formsAlunosAutonomia.html')
@app.route('/AlunoEnsino')
def AlunoEnsino():
    return render_template('formsAlunosQualidadeEnsino.html')
@app.route('/AlunoClima')
def AlunoClima():
    return render_template('formsAlunosClimaEscolar.html')
@app.route('/AlunoInfra')
def AlunosInfra():
    return render_template('formsAlunosInfraestrutura.html')
@app.route('/AlunoGestao')
def AlunosGestao():
    return render_template('formsAlunosGestao.html')

if __name__ == '__main__':
    app.run(debug=True)