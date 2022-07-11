class Robo:
    def __init__(self, nome, fome, saude, idade):
        self.nome = str(nome)
        self.fome =  str(fome)
        self.saude = str(saude)
        self.idade = int(idade)
    def getNome(self):
        self.nome
    def setNome(self, nome):
        self.nome = nome
    def getSaude(self):
        self.saude
    def setSaude(self, saude):
        self.saude = saude
    def getIdade(self):     
        self.idade 
    def setIdade(self, idade):    
        self.idade = idade 
    def alterar(self):
        self.getSaude()   
robo = Robo('Einsten','muita','boa',4)      
print(robo.alterar())
print(vars(robo))
