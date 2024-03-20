from conta import Conta
class ContaPoupanca(Conta):
    def __init__(self, numero, saldo, tipo, taxa_juros):
        super().__init__(numero, saldo)
        self.tipo = tipo
        self.taxa_juros = taxa_juros

    def calcular_juros(self):
        return self.saldo * self.taxa_juros