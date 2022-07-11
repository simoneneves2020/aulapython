class Disciplina:
    def __init__(self, nome, coddiscpl):
        self.nome = nome
        self.coddiscpl = coddiscpl
        self.nota = 0
    def disciplinas(self):
       print('Acesso a lista de disciplinas pelo codigo: ', self.coddiscpl)
    def getdiscipl(self):
        print('nota total das disciplinas', self.nota)
    def setdiscipl(self, n):
        self.nota = n
        print('nota atual da media das disciplinas', self.nota)
    def mostradiscipl(self):
        print(f'A disciplina {self.nome} com o codigo: {self.coddiscpl}')
disciplina = Disciplina('TI',3869)
disciplina.mostradiscipl()
disciplina.disciplinas()
disciplina.getdiscipl()
disciplina.setdiscipl(10)
