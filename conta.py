# -*- coding: utf-8 -*-


class Conta(object):

    def __init__(self, data):
        self.criar_conta(data)

    def criar_conta(self, data):
        try:
            self.numero = data['numero']
            self.titular = data['titular']
            self.saldo = data['saldo']
            self.limite = data['limite']            
        except AttributeError:
            pass # proximo card

    def depositar(self, valor):
        if valor < 0:
            return False
        self.saldo += valor
        return self.saldo

    def sacar(self, valor):
        if self.saldo and self.limite > valor:
            self.saldo -= valor
            return True
        return False

    def extrato(self, conta):
        return "Conta n° {0}, títular {1}, saldo: R$ {2} "\
        "e limite de R$ {3}".format(
            self.numero,
            self.titular,
            self.saldo,
            self.limite)

    def __str__(self):
        return self.numero
