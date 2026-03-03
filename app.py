from flask import Flask

app = Flask(__name__)


@app.route('/')
def home():
    return '<h1>Hello World!</h1>'


@app.route('/<nome>')
def saudacao(nome):
    return f'Olá {nome}'


@app.route('/soma/<n1>/<n2>')
def soma(n1, n2):
    try:
        n1 = int(n1)
        n2 = int(n2)
        return f'{n1} + {n2} = {n1 + n2}'
    except ValueError:
        return f'Apenas números'


@app.route('/subtracao/<n1>/<n2>')
def subtracao(n1, n2):
    try:
        n1 = int(n1)
        n2 = int(n2)
        return f'{n1} - {n2} = {n1 - n2}'
    except ValueError:
        return f'Apenas números'


@app.route('/multiplicacao/<n1>/<n2>')
def multiplicacao(n1, n2):
    try:
        n1 = int(n1)
        n2 = int(n2)
        return f'{n1} * {n2} = {n1 * n2}'
    except ValueError:
        return f'Apenas números'


@app.route('/divisao/<n1>/<n2>')
def divisao(n1, n2):
    try:
        n1 = int(n1)
        n2 = int(n2)
        return f'{n1} / {n2} = {n1 / n2}'
    except ValueError:
        return f'Apenas números'
    except ZeroDivisionError:
        return f'Só números inteiros'

@app.route('/p_i/<numero>')
def verificar(numero):
    try:
        numero = int(numero)
        if numero % 2 == 0:
            return f'O número {numero} é par!'
        else:
            return  f'O número {numero} é ímpar!'
    except ValueError:
        return f'Apenas números inteiros'




if __name__ == '__main__':
    app.run(debug=True, port=5004)
