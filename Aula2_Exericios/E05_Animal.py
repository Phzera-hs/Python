# Sobrescrita de Métodos: 
# Crie uma classe Animal com o método
#  som() que imprime "O animal faz
# um som". 
# Crie classes Cachorro e Gato que
# herdam de Animal e sobrescreva o 
# método som() para
# imprimir sons específicos para cada animal.


class Animal:
    def __init__(self, nome):
        self.nome = nome

    def som(self):
        print("O animal fez um som")

class Cachorro(Animal):
    def __init__(self, nome):
        super().__init__(nome)

    def som(self):
        print(f"O cachorro {self.nome} latiu!")

class Gato(Animal):
    def __init__(self, nome):
        super().__init__(nome)

    def som(self):
        print(f"O gato {self.nome} miou!")

dog = Cachorro("auau")
miau = Gato("miando")
dog.som()
miau.som()