class Funcionario:  
  
    def __init__(self, nome : str, salario : 
        float, aumento : float):    
        self.nome = nome    
        self.salario = salario
        self.aumento = aumento

    def aumentaSalario(self, aumento):    
        self.salario += self.salario*aumento/100   
    
    def mostraFuncionario(self):  
        print(f'Nome: {self.nome}, Salário: {self.salario}, Aumento: {self.aumento}')   

func= Funcionario("Maria", 1500, 100)
func.mostraFuncionario()
func.aumentaSalario(1000)
func.mostraFuncionario()