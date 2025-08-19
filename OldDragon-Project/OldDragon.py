import random
import os



#Utils
class ConsoleUtils():
    def limpar_tela():
        if os.name == 'nt': # Windows
            os.system('cls')
        else: # Linux, macOS, etc.
            os.system('clear')


class Rola_Dados():
    def rolando_d6():
        valor = random.randint(1,6)
        return valor
    
    def rolagem_atributo():        
        i = 0
        soma = 0
        while(i < 3):
            d6 = Rola_Dados.rolando_d6()
            soma += d6
            i += 1
        return soma



# Força, Destreza, Constituição, Inteligência, Sabedoria e Carisma

# ROLANDO ATRIBUTOS
class Estilo_Classico():
    def __init__(self, nome):
        self.nome = nome
        self.forca = 0
        self.destreza = 0
        self.constituicao = 0
        self.inteligente = 0
        self.sabedoria = 0
        self.carisma = 0

class Estilo_Aventureiro():
    def __init__(self, nome):
        self.nome = nome
        self.forca = 0
        self.destreza = 0
        self.constituicao = 0
        self.inteligente = 0
        self.sabedoria = 0
        self.carisma = 0
        self.valores = self.Vetorizacao_Rolagem()
    
    def Vetorizacao_Rolagem(self):
        valores = []
        for i in range(6):
            valores.append(Rola_Dados.rolagem_atributo())
        return valores
    
    def Definindo_Atributos(self):
        print(f"--- Definindo Atributos ---:")
        print(f"Jogador: {self.nome}")
        
        print("Defina os valores:")
        
        while True:
            print(f"\nValores: {self.valores}\n")
            forcaUser = input("Força = ")

            if forcaUser.isdigit():
                valor = int(forcaUser)
                if valor in self.valores:
                    self.forca = valor
                    print(f"Força atribuída = {self.forca}")
                    self.valores.remove(valor)
                    break
                else:
                    print(f"O valor {valor} não está na lista de valores.")
            else:
                print(f"O valor '{forcaUser}' não é um número válido.")
            
        while True:
            print(f"\nValores: {self.valores}\n")
            destrezaUser = input("Destreza = ")
            if destrezaUser.isdigit():
                valor = int(destrezaUser)
                if valor in self.valores:
                    self.destreza = valor
                    print(f"Destreza atribuída = {self.destreza}")
                    self.valores.remove(valor)
                    break
            print(f"O valor '{destrezaUser}' não é válido.")

        while True:
            print(f"\nValores: {self.valores}\n")
            constituicaoUser = input("Constituição = ")
            if constituicaoUser.isdigit():
                valor = int(constituicaoUser)
                if valor in self.valores:
                    self.constituicao = valor
                    print(f"Constituição atribuída = {self.constituicao}")
                    self.valores.remove(valor)
                    break
            print(f"O valor '{constituicaoUser}' não é válido.")

        while True:
            print(f"\nValores: {self.valores}\n")
            inteligenciaUser = input("Inteligência = ")
            if inteligenciaUser.isdigit():
                valor = int(inteligenciaUser)
                if valor in self.valores:
                    self.inteligente = valor
                    print(f"Inteligência atribuída = {self.inteligente}")
                    self.valores.remove(valor)
                    break
            print(f"O valor '{inteligenciaUser}' não é válido.")

        while True:
            print(f"\nValores: {self.valores}\n")
            sabedoriaUser = input("Sabedoria = ")
            if sabedoriaUser.isdigit():
                valor = int(sabedoriaUser)
                if valor in self.valores:
                    self.sabedoria = valor
                    print(f"Sabedoria atribuída = {self.sabedoria}")
                    self.valores.remove(valor)
                    break
            print(f"O valor '{sabedoriaUser}' não é válido.")

        while True:
            print(f"\nValores: {self.valores}\n")
            carismaUser = input("Carisma = ")
            if carismaUser.isdigit():
                valor = int(carismaUser)
                if valor in self.valores:
                    self.carisma = valor
                    print(f"Carisma atribuído = {self.carisma}")
                    self.valores.remove(valor)
                    break
            print(f"O valor '{carismaUser}' não é válido.")


    def Mostrando_Jogador(self):
            ConsoleUtils.limpar_tela()
            print("\n---- FICHA DO JOGADOR ----")
            print(f"Nome: {self.nome}")
            print(f"Força: {self.forca}")
            print(f"Destreza: {self.destreza}")
            print(f"Constituição: {self.constituicao}")
            print(f"Inteligencia: {self.inteligente}")
            print(f"Sabedoria: {self.sabedoria}")
            print(f"Carisma: {self.carisma}")
            
        
        # Força, Destreza, Constituição, Inteligência, Sabedoria e Carisma


    




#Main


nome = input("Digite um nome: ")
Player = Estilo_Aventureiro(nome)
Player.Definindo_Atributos()
Player.Mostrando_Jogador()

    # nome = input("Digite um nome: ")
    # forca = Rola_Dados.rolagem_atributo()
    # destreza = Rola_Dados.rolagem_atributo()
    # constituicao = Rola_Dados.rolagem_atributo()
    # inteligencia = Rola_Dados.rolagem_atributo()
    # sabedoria = Rola_Dados.rolagem_atributo()
    # carisma = Rola_Dados.rolagem_atributo()
    # player = Rola_Dados(nome, forca, destreza, constituicao, inteligencia, sabedoria, carisma)