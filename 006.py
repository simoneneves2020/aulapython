class Quadrado():
    def __init__(self, x):
        self.tamanho_lado = x
    def mudar_val_lado(self, novo_lado):
        x = novo_lado
        self.tamanho_lado = novo_lado
    def retorna_val_lado(self, x):
        self.tamanho_lado = x
        print(x)
    def calc_area(self, x):
        self.tamanho_lado = x
        print(x*x)

carreau = Quadrado(5)
print(carreau.tamanho_lado)

carreau.mudar_val_lado(4)
print(carreau.tamanho_lado)

carreau.retorna_val_lado(3)

carreau.calc_area(5)