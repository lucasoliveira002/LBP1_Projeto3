from flask import*

class Pessoa:
    def __init__(self, id, nome, altura, idade):
        self.id = id
        self.nome = nome
        self.altura = altura
        self.idade = idade

pessoa = Pessoa(1,"raul", 1.80, 17)
