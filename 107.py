class Triangulo:
    def __init__(self, a, b, c):
        self.a = int(a)
        self.b = int(b)
        self.c = int(c)

    def maiorlado(self):
        if (self.a > self.b)and (self.a > self.c):
            print('A é o maior Lado')
        elif (self.b > self.a)and (self.b > self.c):
            print('B é o maior Lado')
        elif (self.c>self.a) and (self.c>self.b):
            print('C é o maior Lado')
    
    def areap(self):
        po = self.a + self.b + self.c
        return po
        print("area ", self.po)
 
p = Triangulo(6, 8, 9)
p.areap()
print(vars(p))
print(p.maiorlado())
print(p.areap())
