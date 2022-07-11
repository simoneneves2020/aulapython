class Tamagotchi:
    def __init__(self, nombre):
        genero = random.choice(["Masculino", "Femenino"])
        print("Tu Tamagotchi es " + genero)
        self.genero = genero
        self.nombre = nombre
        self.hambre = 10
        self.felicidad = 10
        self.salud = 0

    def evento(self, accion):
        self.hambre -= 1
        self.felicidad -= 1
        if accion == "alimentar":
            self.alimentar()
        elif accion == "jugar":
            self.jugar()

    def alimentar(self):
        print("Has alimentado a " + self.nombre)
        self.hambre += 2
        if self.hambre > 10:
            # Sobrealimentado
            self.salud += 2

        pass

    def jugar(self):
        print("Juegas con " + self.nombre)
        self.felicidad += 3
        # Evitar sobrepasar
        if self.felicidad > 10:
            self.felicidad = 10

    def muere(self):
        if self.salud >= 10 or self.felicidad <= 0 or self.hambre <= 0:
            return True
        else:
            return False

    def imprimir_estado(self):
        print("Hambre: " + str(self.hambre))
        print("Felicidad: " + str(self.felicidad))
        print("Salud: " + str(self.salud))