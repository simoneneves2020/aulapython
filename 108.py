class Aluno:
    def __init__(self, nome, cpf, tipodealuno, equipes):
        self.nome = str(nome)
        self.cpf = str(cpf)
        self.tipodealuno = str(tipodealuno)
        self.equipesformadas = int(equipes)
    
    def criarequipe(self):
            self.equipesformadas += 1
         
aluno = Aluno('Ana','1222','A',2)              
print(vars(aluno))
aluno.criarequipe()
print(vars(aluno))
        
    