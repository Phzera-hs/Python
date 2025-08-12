# Polimorfismo com Sobrecarga: Crie uma classe Calculadora com dois métodos somar, um que
# recebe dois inteiros e outro que recebe dois double. Teste os métodos chamando somar com diferentes
# tipos de argumentos.

class Calculadora:
    def somar(self, n1, n2):
        print("SOMA INT")
        print(f"{n1} + {n2} = {n1+n2}")
    
    def somar(self, n1, n2):
        print("SOMA DOUBLE")
        print(f"{n1} + {n2} = {n1+n2}")
    
soma1 = Calculadora()
soma1.somar(2,2)
soma1.somar(5.5,4.5)