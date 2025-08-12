class Veiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def exibir_informacoes(self):
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")

class Carro(Veiculo):
    def __init__(self, marca, modelo, ano):
        super().__init__(marca, modelo)
        self.ano = ano

    def exibir_informacoes(self):
        super().exibir_informacoes()
        print(f"Ano: {self.ano}")

class Esportivo(Carro):
    def __init__(self, marca, modelo, ano, potencia):
        super().__init__(marca, modelo, ano)
        self.potencia = potencia

    def exibir_informacoes(self):
        super().exibir_informacoes()
        print(f"Potência: {self.potencia} cv")

carro = Carro("Toyota", "Corolla", 2020)
esportivo = Esportivo("Ferrari", "F8", 2023, 720)

print("Carro:")
carro.exibir_informacoes()

print("\nEsportivo:")
esportivo.exibir_informacoes()
