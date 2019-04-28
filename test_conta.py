# -*- coding: utf-8 -*-
import pytest
from conta import Conta

conta_123 = Conta(
    numero='123-1',
    titular='Manuela',
    saldo=100.0,
    limite=999.0)


def test_criar_conta():
    assert conta_123.saldo == 100.0 and conta_123.limite == 999.0


def test_depositar_valor_normal():
    conta_123.depositar(12.9)
    assert conta_123.saldo == 112.9


def test_depositar_valor_negativo():
    assert not conta_123.depositar(-1000)


def test_sacar_valor_normal():
    conta_123.sacar(5.87)
    assert conta_123.saldo == 107.03


def test_sacar_valor_negativo():
    assert not conta_123.sacar(-5000)


def test_sacar_valor_acima_do_saldo_e_limite():
    assert not conta_123.sacar(1000)


def test_consultar():
    extrato_conta = conta_123.extrato('123-1')
    str_expected = 'Conta n° 123-1, títular Manuela,'\
        ' saldo: R$ 107.03 e limite de R$ 999.0'
    assert extrato_conta == str_expected


def test_conta_invalida():
    c = Conta()
    assert not c.titular
