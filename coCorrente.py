from conta import Conta

class ContaCorrente(Conta):
    def __init__(self, numero, saldo, tipo):
        super().__init__(numero, saldo)
        self.tipo = tipo
