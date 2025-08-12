from abc import ABC, abstractmethod

class Voador(ABC):
    @abstractmethod
    def voar(self):
        pass

class Nadador(ABC):
    @abstractmethod
    def nadar(self):
        pass

class Pato(Voador, Nadador):
    def voar(self):
        print("O pato está voando!")
    def nadar(self):
        print("O pato está nadando!")

class Aguia(Voador):
    def voar(self):
        print("A águia está voando!")

class Peixe(Nadador):
    def nadar(self):
        print("O peixe está nadando!")

pato = Pato()
aguia = Aguia()
peixe = Peixe()

pato.voar()
pato.nadar()
aguia.voar()
peixe.nadar()
