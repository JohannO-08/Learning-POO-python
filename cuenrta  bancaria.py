class CuentaBancaria:
    def __init__(self,  titular, numeroCuenta, saldo):
        self.titular = titular
        self.numeroCuenta = numeroCuenta
        self.saldo = saldo
        
    def depositar(self):  
        cantidad = int(input("Que cantidad desea depositar"))
        if cantidad <=  0:
         print('cantidad invalida')
        else:
            self.saldo += cantidad
    
    def retirar (self):
        cantidad = int(input("Que cantidad desea retirar "))
        if cantidad > self.saldo:
            print("Fondos Insuficientes")
        else:
            self.saldo -= cantidad
    
    def consultar_saldo (self):
         print ("Titular:", self.titular,
                "Saldo actual: $",self.saldo)
        
    def transferir (self, otra_cuenta, cantidad):
        if cantidad > self.saldo:
            print("No se puede realizar la trasnferencia... Fondos insuficientes")
        else:
            print(self.titular)
            print(otra_cuenta.titular)
            print(cantidad)
            self.saldo -= cantidad
            otra_cuenta.saldo += cantidad
            
            
            
    
    def mostrar_informacion (self ):  
        print("Datos de la cuenta")
        print("Numero de cuenta: ", self.numeroCuenta )
        print("Titular: ", self.titular )
        print("Saldo: ", self.saldo )
        
cuenta1 = CuentaBancaria("Johann", 1001, 32000)
cuenta2 = CuentaBancaria ("Arina", 1002, 0)

cuenta1.consultar_saldo()
cuenta1.depositar()
cuenta1.consultar_saldo()
cuenta1.retirar()
cuenta1.consultar_saldo()
cuenta1.transferir(cuenta2, 5000)
cuenta1.mostrar_informacion()
cuenta2.mostrar_informacion()