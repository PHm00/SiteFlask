from app import app
from flask import render_template
from flask import request

@app.route('/')#configurando uma rotaWeb
@app.route('/index')
def index():
    return render_template('index.html', titulo ="Página Inicial", nome="Pedro")


@app.route('/contato')
def contato():
    return render_template('contato.html', titulo="Contato", nome="Pedro")

@app.route('/ventiladores')
def ventiladores():
    return render_template('ventiladores.html', titulo="Contato", nome="Pedro")
@app.route('/home')
def base():
    return render_template('base.html', titulo="Contato", nome="Pedro")
@app.route('/login')
def login():
    return render_template('login.html', titulo="Comprar", nome="Pedro")

@app.route('/cadastro')
def cadastro():
    return render_template('cadastro.html', titulo="Cadastro", nome="Pedro")