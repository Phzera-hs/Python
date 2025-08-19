import random



#Utils
class Rola_Dados():
    def rolando_d6():
        valor = random.randint(1,6)
        return valor
    
    def rolagem_atributo():        
        i = 0
        while(i < 3):
            soma = 0
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
        print(f"Seus pontos:")
        print(f"Jogador: {self.nome}")
        print(f"Valores: {self.valores}")
        
        print("Defina os valores:")
        
        while True:
            forcaUser = int.input("Força = ")
            if(forcaUser in self.valores):
                    self.forca = forcaUser
                    print(f'Força atribuida = {self.forca}')
                    self.valores.remove(forcaUser)
                    break
            print(f"O valor {forcaUser}, não é válido")
            
        while True:
            destrezaUser = int.input("Destreza = ")
            if(destrezaUser in self.valores):
                    self.forca = destrezaUser
                    print(f'Destreza atribuida = {self.destreza}')
                    self.valores.remove(destrezaUser)
                    break
            print(f"O valor {destrezaUser}, não é válido")

        # Força, Destreza, Constituição, Inteligência, Sabedoria e Carisma

            
        


    




#Main


nome = input("Digite um nome: ")
Estilo_Aventureiro.rolagem_atributo()

player = valor

player = Estilo_Aventureiro.switch()

print(nome)


    # nome = input("Digite um nome: ")
    # forca = Rola_Dados.rolagem_atributo()
    # destreza = Rola_Dados.rolagem_atributo()
    # constituicao = Rola_Dados.rolagem_atributo()
    # inteligencia = Rola_Dados.rolagem_atributo()
    # sabedoria = Rola_Dados.rolagem_atributo()
    # carisma = Rola_Dados.rolagem_atributo()
    # player = Rola_Dados(nome, forca, destreza, constituicao, inteligencia, sabedoria, carisma)