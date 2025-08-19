#  Construtor com Sobrecarga: 
# Crie uma classe Produto com atributos 
# nome e preco. 
# Adicione dois ‘construtores’: 
# um que recebe ambos os atributos 
# e outro que inicializa apenas o nome 
# (sobrecarga de
# construtores, em python, ‘gambiarra’)

class Produto:
    def __init__(self, nome, preco = None):
        self.nome = nome
        self.preco = preco
    
    def imprime_infos(self):
        print(f"Nome: {self.nome}")
        if self.preco is not None:
            print(f"Preço: R${self.preco:.2f}")
        else:
            print("Preço: não definido")

produto = Produto("Mouse", 199.99)
produto2 = Produto("Lápis")

produto.imprime_infos()
produto2.imprime_infos()

