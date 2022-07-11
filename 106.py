class Retangulo:
    def __init__(self, base, altura):
        self._base = base
        self._altura = altura

    @property
    def base(self):
        return self._base

    @base.setter
    def base(self, novo_valor):
        self._base = novo_valor

    @property
    def altura(self):
        return self._altura

    @altura.setter
    def altura(self, novo_valor):
        self._altura = novo_valor

    @property
    def area(self):
        area = float(self._base * self._altura)
        return area

    @property
    def perimetro(self):
        perimetro = 2 * self._base + 2 * self._altura
        return perimetro


