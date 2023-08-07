class Main:
    pass

from Conta import Conta
from Cliente import Cliente

c1 = Cliente("Maria", "3599776-2411")

conta = Conta(c1.nome, 40404, 100000)

print (conta.titular, "\nnumero: ", conta.numero, "\nSeu Saldo: ", conta.saldo)
