from abc import ABC, abstractmethod

class Animal(ABC):
    def dormir(self):
        print("Dormindo... MUITOOOOOO")

    @abstractmethod
    def comer(self):
        pass

class Cachorro(Animal):
    def comer(self):
        print("O cachorro está comendo ração...")

    def latir(self):
        print("Auau!")

class Gato(Animal):
    def comer(self):
        print("O gato está comendo petisco...")

    def miar(self):
        print("Miauuuu...")


dog = Cachorro()
mia = Gato()
miada = Gato()

print("Gato - Mia: ")
mia.comer()
mia.miar()
mia.dormir()
print()
print("Gato - Miada: ")
mia.miar()
mia.dormir()
print()
print("Cachorro - Dog:")
dog.dormir()
dog.comer()
dog.latir()