# -*- coding: utf-8 -*-


class Cliente(object):

    def __init__(
        self,
        nome: str = None,
        sobrenome: str = None,
        cpf: str = None):
        self.nome = nome
        self.sobrenome = sobrenome
        self.cpf = cpf

    def __str__(self):
        return "{} {}".format(self.nome, self.sobrenome)
