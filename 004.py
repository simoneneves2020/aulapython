class Fracao:
    def __init__(self, n=0, d=1):
        self.put(n, d)

    def __str__(self):
        return "%d/%d"%(self.num, self.den)

    def get(self):
        return self.num, self.den

    def put(self, n=0, d=1):
        self.num, self.den = n, d

    def mul(self, other):
        n = self.num * other.num
        d = self.den * other.den
        return Fracao(n, d)

# testes
r1 = Fracao(2)
r2 = Fracao(1,5)
print(r1, '*', r2, '=>', r1.mul(r2))
# teste do div:
# print(r1, '/', r2, '=>', r1.div(r2))
#
# outros testes
