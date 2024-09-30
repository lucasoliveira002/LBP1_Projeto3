from flask import Flask 

class Musica:
    def __init__(self, id, nome, autor, ano):
        self.id = id
        self.nome = nome
        self.autor = autor
        self.ano = ano

playlist = []

def addMusica(nome, autor, ano):
    id = len(playlist) + 1
    nova_musica = Musica(id, nome, autor, ano)
    playlist.append(nova_musica)