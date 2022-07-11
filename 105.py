class Livro:  
      
    def __init__(self, nome, qtdPaginas, autor, preco):    
        self.nome = str(nome)    
        self.qtdPaginas = int(qtdPaginas)   
        self.autor = str(autor)   
        self.preco = float(preco)    
        print(nome,qtdPaginas, autor, preco)
    
    def getPreco(self):    
        print("O preço Original do Livro é :", self.preco)
    #Método para alterar o preço do Livro   
    def setPreco(self, precoNovo):    
         self.preco = precoNovo    
         print("O novo preço do Livro é ", self.preco)

    mostrarlivro = property(getPreco, setPreco)  
livro = Livro("Livro A", 320, "Luis Peixoto", 25)
livro.getPreco()
livro.setPreco(15)
print(vars(livro))
