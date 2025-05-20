from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def ola():
    return render_template('index.html')


@app.route('/sobre-equipe')
def sobreEquipe():
    return render_template('sobre-equipe.html')


@app.route('/variaveis')
def variaveis():
    return render_template('variaveis.html')

@app.route('/tipos-dados')
def tipos_dados():
    return render_template('tipos-dados.html')

@app.route('/estruturas-controle')
def estruturas_controle():
    return render_template('estruturas-controle.html')

@app.route('/funcoes')
def funcoes():
    return render_template('funcoes.html')

@app.route('/listas')
def listas():
    return render_template('listas.html')

@app.route('/dicionarios')
def dicionarios():
    return render_template('dicionarios.html')


app.run(debug=True)