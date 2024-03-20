from conta import Conta

class ContaCorrente(Conta):
    def _init_(self, numero, saldo, tipo):
        super()._init_(numero, saldo)
        self.tipo = tipo
