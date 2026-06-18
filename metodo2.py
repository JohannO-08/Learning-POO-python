#cuenta banaria

class CuentaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo  
        
    def depositar(self, cantidad):
        self.saldo += cantidad
  
    def retirar(self, cantidad):
        if cantidad <= self.saldo:
            self.saldo -= cantidad
        else:
            print("Fondos insuficientes.") 
        
cuneta1 = CuentaBancaria( "Johann", 10500.0)
cuneta2 = CuentaBancaria( "keilin", 8000.0)

cuneta1.depositar (5000)
cuneta1.depositar (2000)
cuneta1.depositar (1000)
cuneta1.depositar (3200)
cuneta1.retirar(20000)
print("El sald0 final es de", cuneta1.saldo)