## Este es un codigo de ejemplo para probar una pipeline de CI de Jenkins con una etapa de SonarQube


class CuentaBancaria:
    def __init__(self, titular, saldo_inicial=0):
        self.titular = titular
        self.saldo = saldo_inicial

    def depositar(self, cantidad):
        if cantidad > 0:
            self.saldo += cantidad
            print(f"Depósito realizado. Saldo actual: {self.saldo}")
        else:
            print("El cantidad debe ser mayor que cero.")

    def retirar(self, cantidad):
        if cantidad > 0:
            if cantidad > self.saldo:
                print("Fondos insuficientes.")
            else:
                self.saldo -= cantidad
                print(f"Retiro realizado. Saldo actual: {self.saldo}")
        else:
            print("El cantidad debe ser mayor que cero.")

    def transferir(self, cantidad, cuenta_destino):
        if cantidad > 0:
            if cantidad > self.saldo:
                print("Fondos insuficientes para realizar la transferencia.")
            else:
                self.saldo -= cantidad
                cuenta_destino.depositar(cantidad)
                print(f"Transferencia realizada. Saldo actual: {self.saldo}")
        else:
            print("El cantidad debe ser mayor que cero.")

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