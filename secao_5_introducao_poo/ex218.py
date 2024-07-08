class Carro:
    def __init__(self, nome):
        self.nome = nome
        self._motor = None
        self._fabricante = None

    def lista_carro(self):
        print(self.nome, self.motor.nome, self.fabricante.nome)

    @property
    def motor(self):
        return self._motor
    
    @motor.setter
    def motor(self, valor):
        self._motor = valor

    @property
    def fabricante(self):
        return self._fabricante
    
    @fabricante.setter
    def fabricante(self, valor):
        self._fabricante = valor

class Motor:
    def __init__(self, nome):
        self.nome = nome

class Fabricante:
    def __init__(self, nome):
        self.nome = nome

fusca = Carro("Fusca")
motor_1_0 = Motor("1.0")
volkswagem = Fabricante("Volkswagem")

fusca.fabricante = volkswagem
fusca.motor = motor_1_0

fusca.lista_carro()

uno = Carro("Uno")
fiat = Fabricante("Fiat")

uno.fabricante = fiat
uno.motor = motor_1_0

uno.lista_carro()