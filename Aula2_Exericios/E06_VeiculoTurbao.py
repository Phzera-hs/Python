# 6. Herança em Cadeia: 
# Crie uma classe Veiculo com um método mover(). 
# Crie uma classe Carro que
# herda de Veiculo e adiciona o método abastecer(). 
# Em seguida, crie uma classe Esportivo que herda de
# Carro e adiciona o método turbo

class Veiculo():

    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
    
    def mover(self):
        print("Andando...")

class Carro(Veiculo):
    def __init__(self, marca, modelo):
        super().__init__(marca, modelo)


    #mover()?

    def abastecer(self):
        print("Abastecendo...")
    
class Esportivo(Carro):
    def __init__(self, marca, modelo):
        super().__init__(marca, modelo)

    def turbo(self):
        print("VRUMMMMM")

carro = Esportivo("Honda", "Civic")
carro.mover()
carro.abastecer()
carro.turbo()