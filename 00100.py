class Clienteconta:
    def __init__(self,  nome, telefone, numero, saldo, limite):
        self.nome = str(nome)
        self.telefone = str(telefone)
        self.numero = str(numero)
        self.saldo = saldo
        self.limite = limite
        # inicia extrato
        self.extrato = []

    def saque(self, valor):
        if valor < (self.saldo + self.limite):
            self.saldo -= valor
            # adiciona ao extrato
            self.extrato.append("- Saque: " + str(valor))
            return valor
        else:
            print ('Saldo insuficiente')

    def deposito(self, valor):
        self.saldo += valor
        # adiciona ao extrato
        self.extrato.append("+ Deposito: " + str(valor))

    def extrato(self):
        print ('------Extrato------')
        print('Conta: ', self.numero+'\n')
        for i in self.extrato:
            print( i + '\n')
        print('Saldo: ', self.saldo)
        print ('Limite: ', self.limite)
        print ('Disponivel: ', self.saldo+self.limite)


    def mostraCliente(self):  
        print(f'Nome: {self.nome}, telefone: {self.telefone}, Numero: {self.numero}, Saldo: {self.saldo}, limite: {self.limite}')
                
teste = Clienteconta('Ana','90999-0000',10029, 100.00, 3000.00)


teste.mostraCliente()
teste.saque(80)
teste.deposito(1200)

teste.mostraCliente()


