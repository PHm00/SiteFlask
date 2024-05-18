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
@app.route('/ventilador1')
def ventilador1():
    return render_template('indexVentila1.html', titulo="Ventilador1", nome="Pedro")
@app.route('/ventilador2')
def ventilador2():
    return render_template('indexVentila2.html', titulo="Ventilador2", nome="Pedro")
@app.route('/ventilador3')
def ventilador3():
    return render_template('indexVentila3.html', titulo="Ventilador2", nome="Pedro")
@app.route('/ellonMusk')
def ellonMusk():
    return render_template('ElonMusk.html', titulo="ElonMusk", nome="Pedro")
@app.route('/ellonMusk1')
def ellonMusk1():
    return render_template('EllonMusko.html', titulo="ElonMusk", nome="Pedro")
