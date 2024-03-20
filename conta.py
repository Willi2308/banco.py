class Conta:
    def __init__(self, numero, saldo):
        self.numero = numero
        self.saldo = saldo
        self.transacoes = []

    def depositar(self, valor):
        self.saldo += valor
        self.registrar_transacao(f"Depósito de R${valor}")

    def sacar(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
            self.registrar_transacao(f"Saque de R${valor}")
        else:
            print("Saldo insuficiente para saque.")

    def registrar_transacao(self, descricao):
        self.transacoes.append(descricao)

    def extrato(self):
        print(f"Extrato da conta {self.numero}:")
        for transacao in self.transacoes:
            print(transacao)