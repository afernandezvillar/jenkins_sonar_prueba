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


