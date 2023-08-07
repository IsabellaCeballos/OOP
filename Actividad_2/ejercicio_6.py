#Cree una clase CuentaBancaria que contenga los siguientes atributos: numero_cuenta, propietarios y balance. Los tres atributos se deben inicializar en el constructor con valores recibidos como parámetros.
#Para la clase CuentaBancaria, cree un método depositar que maneje las acciones de depósito en la cuenta.
#Para la clase CuentaBancaria, cree un método retirar que maneje las acciones de retiro de la cuenta.
#Para la clase CuentaBancaria, cree un método aplicar_cuota_manejo que aplique un porcentaje del 2% sobre el balance de la cuenta
#Para la clase CuentaBancaria, cree un método mostrar_detalles que imprima por consola los detalles de la cuenta bancaria.

class Cuenta_Bancaria:
    def __init__(self, num_cuenta, propietarios, balance):
        self.num_cuenta = num_cuenta
        self.propietarios = propietarios
        self.balance = balance
    
    def depositar(self, cantidad):
        self.balance += cantidad
    
    def retirar(self, cantidad):
        if cantidad <= self.balance:
            self.balance -= cantidad
        else:
            print("Saldo insuficiente.")
    
    def cuota_manejo(self):
        cuota = self.balance * 0.02
        self.balance -= cuota
    
    def mostrar_detalles(self):
        print("Número de cuenta:", self.num_cuenta)
        print("Propietarios:", ', '.join(self.propietarios))
        print("Balance:", self.balance)

# Ejemplo de uso
cuenta = Cuenta_Bancaria("170905", ["Isabella", "Pablo"], 500000000)
cuenta.mostrar_detalles()

cuenta.depositar(500000)
cuenta.mostrar_detalles()

cuenta.retirar(150000)
cuenta.mostrar_detalles()

cuenta.cuota_manejo()
cuenta.mostrar_detalles()
