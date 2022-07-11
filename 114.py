class Robo:
    def __init__(self, nome: str, saude: int, fome: str, idade: int):
        self.nome = nome
        self.saude = saude
        self.idade = idade
        self.fome = fome
    def getaltnome(self):
         print("get nome", self.nome)
    def setaltnome(self, n):
        self.nome = n
        print("set nome", self.nome)
    def getaltsaude(self):
        print("get saude",self.saude)
    def setaltsaude(self, s):
        self.saude = s
        print("set saude", self.saude)
    def getaltidade(self):
        print("get idade",self.idade)
    def setaltidade(self, i):
        self.idade = i
    def mostrarobo(self):
        print({self.nome},"está com a saude em: ",{self.saude}, "é com fome ?", {self.fome}, "com a idade", {self.idade})
    testmostra = (getaltnome, setaltnome, getaltsaude, setaltsaude, getaltidade, setaltidade)

test = Robo("Leo", 100, "não", 10)
test.mostrarobo()
test.setaltnome("Rikard")
test.setaltsaude(60)
test.setaltidade(11)
test.mostrarobo()
