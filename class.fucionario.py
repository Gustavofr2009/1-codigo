class fucionario:
    def __init__(self, nome, salario__base):
        self.nomr = nome
        self.salario__base = salario__base
    def calcular__salario(self):
        return self.salario__base
class gerente(fucionario):
    def __init__(self, nome, salario__base, bonus):
        super().__init__(nome, salario__base)
        self.bonus = bonus
    def calcular__salario(self):
        return self.salario__base + self.bonus