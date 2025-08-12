# Exercícios sobre Polimorfismo
# 8. Polimorfismo com Herança: 
# Crie uma classe Forma com um método 
# calcularArea(). Crie classes
# Circulo e Quadrado que herdam de
# Forma e sobrescrevem o método para
# calcular a área específica de
# cada forma. 
# Pense em como o polimorfismo pode 
# ajudar calcular áreas de diferentes 
# formas em uma
# lista de ‘Formas


class Forma:
    def calcular_area(self):
        pass

class Circulo(Forma):

    def calcular_area(self, raio):
         A = 3.13 * (raio*raio)
         return A
    
class Quadrado(Forma):
    def calcular_area(self, lado):
        A = lado * lado
        return A
    
quadrado = Quadrado()
circulo = Circulo()

print(f"Quadrado = {quadrado.calcular_area(2)}")
print(f"Circulo = {circulo.calcular_area(2)}")