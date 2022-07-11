class Aluno:
    def __init__(self, nome : str, curso : str,	temposemdormir : int, 
    qtdhorasestudo : int):
        self.nome = nome
        self.curso = curso
        self.temposemdormir = temposemdormir
        self.qtdhorasestudo = qtdhorasestudo
    
    def estudar(self,temposemdormir):
        self.temposemdormir -= 2
    
    def dormir(self, qtdhorasestudo):
        self.qtdhorasestudo += 4
        
    def mostraAluno(self):  
        print(f'Nome: {self.nome}, curso: {self.curso}, TempoSemDormir: {self.temposemdormir}, QtdHoras: {self.qtdhorasestudo}')
                
teste = Aluno('Ana','TI',8, 6)

teste.mostraAluno()
teste.estudar(10)
teste.dormir(4)
teste.mostraAluno()



