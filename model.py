
class CuentaBancaria:
    def __init__(self, titular, saldo_inicial=0):
        self.titular = titular
        self.saldo = saldo_inicial

    def depositar(self, monto):
        if monto > 0:
            self.saldo += monto
            print(f"Depósito realizado. Saldo actual: {self.saldo}")
        else:
            print("El monto debe ser mayor que cero.")

    def retirar(self, monto):
        if monto > 0:
            if monto > self.saldo:
                print("Fondos insuficientes.")
            else:
                self.saldo -= monto
                print(f"Retiro realizado. Saldo actual: {self.saldo}")
        else:
            print("El monto debe ser mayor que cero.")

    def transferir(self, monto, cuenta_destino):
        if monto > 0:
            if monto > self.saldo:
                print("Fondos insuficientes para realizar la transferencia.")
            else:
                self.saldo -= monto
                cuenta_destino.depositar(monto)
                print(f"Transferencia realizada. Saldo actual: {self.saldo}")
        else:
            print("El monto debe ser mayor que cero.")

    def consultar_saldo(self):
        print(f"Saldo actual: {self.saldo}")


# Ejemplo de uso
cuenta1 = CuentaBancaria("Juan Perez", 1000)
cuenta2 = CuentaBancaria("Maria Lopez", 500)

cuenta1.consultar_saldo()
cuenta2.consultar_saldo()

cuenta1.depositar(500)
cuenta1.retirar(200)

cuenta1.consultar_saldo()

cuenta1.transferir(300, cuenta2)

cuenta1.consultar_saldo()
cuenta2.consultar_saldo()