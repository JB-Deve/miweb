# reforzamiento
import os
os.system("cls")

class CuentaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo
    
    def depositar(self, cantidad):
        self.saldo += cantidad
        print(f"Has depositado: {cantidad}. Nuevo saldo: {self.saldo}")

    def retirar(self, cantidad):
        if self.saldo >= cantidad:
            self.saldo -= cantidad
            print(f"Has retirado: {cantidad}. Nuevo saldo: {self.saldo}")
        else:
            print(f"Fondos insuficientes. Saldo actual: {self.saldo}")
            
    def mostrar_saldo(self):
        print(f"{self.titular}, tu saldo actual es de: {self.saldo}")


c1 = CuentaBancaria("Jota", 2000)
c2 = CuentaBancaria("Pedro", 1799)
c3 = CuentaBancaria("Carla", 2500)
c4 = CuentaBancaria("Igor", 700)
c5 = CuentaBancaria("Lee", 2750)

titulares_banco = [c1, c2, c3, c4, c5]

for i in titulares_banco:
    i.mostrar_saldo()
    print("-" * 50)
# titulares_banco.depositar()
