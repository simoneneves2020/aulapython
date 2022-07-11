class Pessoa:
    def __init__(self, nome: str,idade: int, altura: float):
        self.nome = nome
        self.idade = idade
        self.altura = altura

    def mostraPessoa(self):
        print(f'Nome: {self.nome}, Idade: {self.idade},altura: {self.altura} ')

pessoa = Pessoa(nome='João', idade =25, altura=1.88)
pessoa.mostraPessoa()


    
 