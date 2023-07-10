## Codigo de ejemplo para probar una pipeline de integración de Jenkins con SonarQube
##
## Descripcion: La clase CuentaBancaria permite simular la creacion de una cuenta bancaria para una persona determinada
## con un salario determinado. Cada objeto CuentaBancaria tiene varios métodos.
##
## ---------------------------------------------------------------------------------


class CuentaBancaria:
    def __init__(self, titular, saldo_inicial=0):
        self.titular = titular
        self.saldo = saldo_inicial

    def depositar(self, monto):
        if monto > 0:
            self.saldo += monto
            print(f"Depósito realizado. Saldo actual: {self.saldo}")
        else:
            print("La cantidad debe ser mayor que cero.")

    def retirar(self, monto):
        if monto > 0:
            if monto > self.saldo:
                print("Fondos insuficientes.")
            else:
                self.saldo -= monto
                print(f"Retiro realizado. Saldo actual: {self.saldo}")
        else:
            print("La cantidad debe ser mayor que cero.")

    def transferir(self, monto, cuenta_destino):
        if monto > 0:
            if monto > self.saldo:
                print("Fondos insuficientes para realizar la transferencia.")
            else:
                self.saldo -= monto
                cuenta_destino.depositar(monto)
                print(f"Transferencia realizada. Saldo actual: {self.saldo}")
        else:
            print("La cantidad debe ser mayor que cero.")

    def consultar_saldo(self):
        print(f"Saldo actual: {self.saldo}")


# Ejemplo de uso
cuenta1 = CuentaBancaria("Alvaro Cuenta 1", 1000)
cuenta2 = CuentaBancaria("Alvaro Cuenta 2", 500)

cuenta1.consultar_saldo()
cuenta2.consultar_saldo()

cuenta1.depositar(500)
cuenta1.retirar(200)

cuenta1.consultar_saldo()

cuenta1.transferir(300, cuenta2)

cuenta1.consultar_saldo()
cuenta2.consultar_saldo()