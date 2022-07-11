class Robo:
    def __init__(self, nome: str, idade: int, fome: str, saude: str):
        self.nome = nome
        self.idade = idade
        self.fome = fome
        self.saude = saude
        print(nome, idade, fome, saude)

    def getIdade(self):
        print('get idade', self.idade)
    
    def setIdade(self):
        print('set idade', self.idade)

    def getFome(self):
        print('get fome', self.fome)
    
    def setFome(self):
        print('set fome', self.fome)

    def getSaude(self):
        print('get saude', self.saude)
    
    def setSaude(self):
        print('set saude', self.saude)
    
    mostraelementos = property(getFome, setFome, getSaude, setSaude)
meurobo = Robo('Ominitrix', 5, 'Muita fome', 'Saúde ruim')
meurobo.getFome()
meurobo.setFome()
meurobo.getSaude()
meurobo.setSaude()
print(vars(meurobo)) 


