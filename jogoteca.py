from flask import Flask , render_template

app = Flask(__name__)

class Jogo:
    def __init__(self, nome, categoria, plataforma):
        self.nome = nome
        self.categoria = categoria
        self.plataforma = plataforma

@app.route('/inicio')
def ola():
    jogo1 = Jogo('World of Warcraft', 'MMO', 'PC')
    jogo2 = Jogo('Final Fantasy XIV', 'MMO', 'PC')
    jogo3 = Jogo('The Elder Scrolls', 'RPG', 'PC')
    lista = [jogo1, jogo2, jogo3]
    return render_template('lista.html', titulo='Jogos', jogos=lista)

@app.route('/novo')
def novo():
    return render_template('novo.html', titulo='Novo jogo')


app.run()

