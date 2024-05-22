from app import app
from flask import render_template
from flask import request
import json
import requests

link = "https://pedroflaskti18n-default-rtdb.firebaseio.com/" #conectar banco de dados
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
@app.route('/cadastrarUsuario', methods=['POST'])
def cadastrarUsuario():
    try:
        cpf     = request.form.get("cpf")
        nome    = request.form.get("nome")
        telefone = request.form.get("telefone")
        endereco = request.form.get("endereco")
        dados    = {"cpf":cpf,"nome":nome,"telefone":telefone,"endereco":endereco}
        requisicao = requests.post(f'{link}/cadastrar/.json', data=json.dumps(dados))
        return 'cadastrado com sucesso'

    except Exception as e:
        return f'Ocorreu um erro\n\n + {e}'

@app.route('/listar')
def listarTudo():
        try:
            requisicao = requests.get(f'{link}/cadastrar/.json')
            dicionario = requisicao.json()
            return dicionario
        except Exception as e:
            return f' Ocorreu um erro\n\n + {e}'
@app.route('/listarIndividual')
def listarIndividual():
    try:
        requisicao = requests.get(f'{link}/cadastrar/.json')
        dicionario = requisicao.json()
        idCadastro = ""
        usuario = ""
        for codigo in dicionario:
            usuario = dicionario[codigo]['telefone']
            if usuario == "123":
                idCadastro = codigo

        return idCadastro
    except Exception as e:
        return f'Algo deu errado!\n\n + {e}'
@app.route('/atualizar')
def atualizar():
    try:
        dados = {"nome":"Nayara"}#Parametro
        requisicao = requests.patch(f'{link}/cadastrar/-NySNCQ9tmLdQW9tlUpg/.json', data=json.dumps(dados))
        return "Atualizado com sucesso!"

    except Exception as e:
        return f'Houve um erro!\n\n + {e}'
@app.route('/excluir')
def excluir():
    try:
        requisicao = requests.delete(f'{link}/cadastrar/-NySNCQ9tmLdQW9tlUpg/.json')
        return "Excluído com sucesso"

    except Exception as e:
        return f'Houve um erro!\n\n + {e}'

