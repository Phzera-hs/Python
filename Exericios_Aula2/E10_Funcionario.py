
#  Classes Abstratas: Crie uma classe abstrata Funcionario com um método abstrato calcularSalario().
# Implemente duas subclasses, FuncionarioHorista e FuncionarioMensalista, que implementam o cálculo
# de salários de acordo com o tipo de funcionário

from abc import ABC, abstractmethod

class Funcionario(ABC):

    @abstractmethod
    def calcularSalario(self):
        pass


class FuncionarioMensalista(Funcionario):
    def __init__(self, nome, salario_mensal):
        self.nome = nome
        self.salario_mensal = salario_mensal

    def calcularSalario(self):
        return self.salario_mensal


class FuncionarioHorista(Funcionario):
    def __init__(self, nome, horas_trabalhadas, valor_hora):
        self.nome = nome
        self.horas_trabalhadas = horas_trabalhadas
        self.valor_hora = valor_hora

    def calcularSalario(self):
        return self.horas_trabalhadas * self.valor_hora


# Teste
f1 = FuncionarioMensalista("João", 3000)
f2 = FuncionarioHorista("Maria", 160, 20)

print(f"{f1.nome} recebe R${f1.calcularSalario():.2f}")
print(f"{f2.nome} recebe R${f2.calcularSalario():.2f}")
