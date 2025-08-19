# Exercícios sobre Herança
# 4. Herança Simples: 
# Crie uma classe Funcionario com atributos 
# nome e salario. 
# Em seguida, crie uma
# classe Gerente que herda de 
# Funcionario e adicione o atributo 
# departamento. Adicione um método para
# exibir as informações do gerente

class Funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario

class Gerente(Funcionario):
    def __init__(self, nome, salario, departamento):
        super().__init__(nome, salario)
        self.departamento = departamento
    
    def imprime_infos(self):
        print(f"Nome: {self.nome}")
        print(f"Salario: {self.salario}")
        print(f"Departamento: {self.departamento}")


pessoa = Gerente("Paulinho", 2, "T.I")
pessoa.imprime_infos()