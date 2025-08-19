#  Métodos e Atributos: 
# Crie uma classe Carro 
# com os atributos marca, modelo e ano.
#  Adicione
# métodos para alterar e obter esses valores.
#  Inclua também um método para exibir
#  as informações do
# carro

class Carro:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
    
    def getMarca(self, marca):
        return self.marca
    
    def setMarca(self, marca):
        self.marca = marca

    def getModelo(self, modelo):
        return self.modelo
    
    def setModelo(self, modelo):
        self.modelo = modelo

    def getAno(self, ano):
        return self.ano
    
    def setAno(self, ano):
        self.ano = ano

    def exibir_info(self):
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Ano: {self.ano}")

carro = Carro("Honda", "Fit", 2022)
carro.exibir_info()
carro.setModelo("Civic")
carro.setAno(2009)
print("---- CARRO ALTERADO ----")
carro.exibir_info()
