from cliente import Cliente
from coCorrente import CheckingAccount
from coPoupanca import SavingAccount

client1 = Cliente("João da Silva", "123.456.789-01")
client2 = Cliente("Maria dos Santos", "987.654.321-02")

checking1 = CheckingAccount(1, 5000, "Corrente")
saving1 = SavingAccount(2, 10000, "Poupança", 0.05)
saving2 = SavingAccount(3, 15000, "Poupança", 0.07)

client1.add_account(checking1)
client2.add_account(saving1)
client2.add_account(saving2)

checking1.deposit(300)
checking1.withdraw(1000)
saving1.deposit(1000)
saving1.calculate_interest()
saving2.deposit(5000)
saving2.calculate_interest()

print(checking1)
checking1.extract()
print(saving1)
saving1.extract()
print(saving2)
saving2.extract()