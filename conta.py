# -*- coding: utf-8 -*-

from cliente import Cliente

class Conta(object):

    def __init__(
        self,
        numero: str = None,
        titular: object = None,
        saldo: float = 0.0,
        limite: float = 0.0
    ):

        try:
            self.numero = numero
            self.titular = titular
            self.saldo = saldo
            self.limite = limite
        except Exception:
            return False

    def depositar(self, valor):
        if valor < 0:
            return False
        self.saldo += valor
        return self.saldo

    def sacar(self, valor):
        if self.saldo and self.limite > valor and valor > 0:
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

    def transferir_para(self, conta_destino: object, valor: float):
        sacar = self.sacar(valor)
        if not sacar:
            return False

        conta_destino.depositar(valor)

    def __str__(self):
        return self.numero
