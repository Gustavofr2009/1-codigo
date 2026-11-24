class animal:
    def __init__(self, nome):
        self.nome = nome
    def fazer__som(self):
        return "..."

class cachorro(animal):
    def fazer__som(self):
        return  f"{self.nome} diz: Au Au!"

class gato(animal):
    def fazer__som(self):
        s = super().fazer__som()
        return f"{self.nome} diz: Miau! ({s})"

animais = [cachorro("Rex"), gato("Yuumi")]
for a in animais:
    print(a.fazer__som())