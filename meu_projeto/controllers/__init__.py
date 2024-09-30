from flask import Blueprint, render_template, request, redirect, url_for
from models import playlist, addMusica

playlist_controller = Blueprint('musica', __name__)

@playlist_controller.route('/')
def index():
    return render_template('index.html', playlist = playlist)

@playlist_controller.route('/add', methods=['POST'])
def add():
    nome = request.form['nome']
    autor = request.form['autor']
    ano = request.form['ano']
    addMusica(nome, autor, ano)
    return redirect(url_for('musica.index'))