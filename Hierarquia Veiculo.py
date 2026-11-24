class Veiculo:
    def __init__(self, marca, velocidade_max):
        self.marca = marca
        self.velocidade_max = velocidade_max

    def mover(self):
        print("O veículo está se movendo.")


class Carro(Veiculo):
    def __init__(self, marca, velocidade_max, num_portas):
        super().__init__(marca, velocidade_max)
        self.num_portas = num_portas

    def mover(self):
        print(f"O carro {self.marca} está acelerando!")


class Bicicleta(Veiculo):
    def __init__(self, marca, velocidade_max, num_marchas):
        super().__init__(marca, velocidade_max)
        self.num_marchas = num_marchas

    def mover(self):
        print(f"A bicicleta {self.marca} está pedalando!")


carro = Carro("Toyota", 200, 4)
bicicleta = Bicicleta("Caloi", 40, 21)

print("Carro:")
print("Marca:", carro.marca)
print("Velocidade máxima:", carro.velocidade_max)
print("Número de portas:", carro.num_portas)
carro.mover()

print("\nBicicleta:")
print("Marca:", bicicleta.marca)
print("Velocidade máxima:", bicicleta.velocidade_max)
print("Número de marchas:", bicicleta.num_marchas)
bicicleta.mover()