from model import CuentaBancaria
import pytest


@pytest.fixture
def cuentas():
    cuenta1 = CuentaBancaria("Juan Perez", 1000)
    cuenta2 = CuentaBancaria("Maria Lopez", 500)
    return cuenta1, cuenta2


def test_depositar(cuentas):
    cuenta1, _ = cuentas
    cuenta1.depositar(500)
    assert cuenta1.saldo == 1500


def test_retirar(cuentas):
    _, cuenta2 = cuentas
    cuenta2.retirar(200)
    assert cuenta2.saldo == 300


def test_transferir(cuentas):
    cuenta1, cuenta2 = cuentas
    cuenta1.transferir(500, cuenta2)
    assert cuenta1.saldo == 500
    assert cuenta2.saldo == 1000


def test_retirar_fondos_insuficientes(cuentas):
    cuenta1, _ = cuentas
    cuenta1.retirar(2000)
    assert cuenta1.saldo == 1000


def test_transferir_fondos_insuficientes(cuentas):
    cuenta1, cuenta2 = cuentas
    cuenta1.transferir(2000, cuenta2)
    assert cuenta1.saldo == 1000
    assert cuenta2.saldo == 500


def test_depositar_monto_negativo(cuentas):
    cuenta1, _ = cuentas
    cuenta1.depositar(-200)
    assert cuenta1.saldo == 1000


def test_retirar_monto_negativo(cuentas):
    _, cuenta2 = cuentas
    cuenta2.retirar(-500)
    assert cuenta2.saldo == 500


def test_transferir_monto_negativo(cuentas):
    cuenta1, cuenta2 = cuentas
    cuenta1.transferir(-300, cuenta2)
    assert cuenta1.saldo == 1000
    assert cuenta2.saldo == 500

