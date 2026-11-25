import math

class Figura:
    def calcular_area(self):
        pass

class Retangulo(Figura):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        return self.base * self.altura

class Circulo(Figura):
    def __init__(self, raio):
        self.raio = raio

    def calcular_area(self):
        return math.pi * (self.raio ** 2)

figuras = [
    Retangulo(5, 3),
    Circulo(4),
    Retangulo(6, 2),
    Circulo(3)
]
for figura in figuras:
    print(f"Área: {figura.calcular_area():.2f}")
