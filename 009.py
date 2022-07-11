class Cliente:
    def __init__(self, nome, telefone):
        self.nome = nome
        self.telefone = telefone

class Conta:
    def __init__(self, cliente, numero, saldo = 0):
        self.numero = str(numero)
        self.saldo = 0
        self.cliente = cliente
        self.operacoes = []
        self.deposito(saldo)

    def deposito(self, valor):
        self.saldo += valor
        self.operacoes.append(["Deposito", valor])


from conta import Conta
class Limite(Conta):
    def __init__(self,cliente, numero, saldo = 0, limite = 0):
        Conta.__init__(self, cliente, numero, saldo)
        self.limite = limite

    def saque(self, valor=0):
        if valor <= self.limite + self.saldo:
            self.saldo -= valor
            self.operacoes.append(["Saque", valor])
        else:
            print("Saldo Insuficiente\n")

def extrato(self):

    print("CC Numero: %s" % self.numero)
    for a in self.operacoes:
        print ("%-10s %10.2f" % (a[0], a[1]))

    print("Saldo \t %12.2f" % self.saldo)
    print("Lim. Especial \t %4.2f" % self.limite)
    print("Disponivel \t %8.2f" % int(self.limite + self.saldo)+"\n")