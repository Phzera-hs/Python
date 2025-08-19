from abc import ABC, abstractmethod
import random


# Interfaces para estratégias

class ComportamentoVoo(ABC):
    @abstractmethod
    def voar(self):
        pass

class ComportamentoGrasnar(ABC):
    @abstractmethod
    def grasnar(self):
        pass

# Implementações concretas de voo

class VoarComAsas(ComportamentoVoo):
    def voar(self):
        print("Voando com asas!")

class NaoVoar(ComportamentoVoo):
    def voar(self):
        print("Não posso voar.")

class VoarComFoguete(ComportamentoVoo):
    def voar(self):
        print("Voando com foguete! 🚀")

class VooAleatorio(ComportamentoVoo):
    def voar(self):
        opcoes = [
            "Tentou voar mas caiu rindo no chão 😂",
            "Voando em círculos... ou não? 🌀",
            "Voando com foguete imaginário! 💨",
            "Ficou deitado olhando o céu ☁️"
        ]
        print(random.choice(opcoes))


# Implementações concretas de grasnar

class GrasnarNormal(ComportamentoGrasnar):
    def grasnar(self):
        print("Quack!")

class GrasnarMudo(ComportamentoGrasnar):
    def grasnar(self):
        print("... (silêncio)")

class GrasnarRobotico(ComportamentoGrasnar):
    def grasnar(self):
        print("Qu4ck 8!p b33p!")

class GrasnarViajado(ComportamentoGrasnar):
    def grasnar(self):
        sons = [
            "Quaaaack... ou foi um eco? 🌀",
            "Qrk blup zzz... 🌈",
            "Quack quack boom 🎇",
            "*risos* kkkkkk",
            "Grasnando com as estrelas ✨"
        ]
        print(random.choice(sons))


# Classe base Pato

class Pato:
    def __init__(self, comportamento_voo: ComportamentoVoo, comportamento_grasnar: ComportamentoGrasnar):
        self.comportamento_voo = comportamento_voo
        self.comportamento_grasnar = comportamento_grasnar

    def nadar(self):
        print("Nadando como um pato.")

    def exibir(self):
        print("Sou um pato genérico.")

    def performar_voo(self):
        self.comportamento_voo.voar()

    def performar_grasnar(self):
        self.comportamento_grasnar.grasnar()

    def set_comportamento_voo(self, novo_voo: ComportamentoVoo):
        self.comportamento_voo = novo_voo

    def set_comportamento_grasnar(self, novo_grasnar: ComportamentoGrasnar):
        self.comportamento_grasnar = novo_grasnar

# Subclasses específicas de pato

class PatoReal(Pato):
    def exibir(self):
        print("Sou um Pato Real!")

class PatoDeBorracha(Pato):
    def exibir(self):
        print("Sou um Pato de Borracha!")

class PatoDrogado(Pato):
    def exibir(self):
        print("Sou um Pato Drogado... calma, tá tudo bem 😵‍💫")

# Testando

if __name__ == "__main__":
    pato1 = PatoReal(VoarComAsas(), GrasnarNormal())
    pato2 = PatoDeBorracha(NaoVoar(), GrasnarMudo())
    pato_drogado = PatoDrogado(VooAleatorio(), GrasnarViajado())

    print("=== Pato Real ===")
    pato1.exibir()
    pato1.performar_voo()
    pato1.performar_grasnar()

    print("\n=== Pato de Borracha ===")
    pato2.exibir()
    pato2.performar_voo()
    pato2.performar_grasnar()

    print("\nAgora o Pato de Borracha aprende a voar com foguete:")
    pato2.set_comportamento_voo(VoarComFoguete())
    pato2.set_comportamento_grasnar(GrasnarRobotico())
    pato2.performar_voo()
    pato2.performar_grasnar()

    print("\n=== Pato Drogado ===")
    pato_drogado = PatoDrogado(VooAleatorio(), GrasnarViajado())
    pato_drogado.exibir()
    pato_drogado.performar_grasnar()
    print("---")


