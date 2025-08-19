idadeTxt = input("Digite as idades: ")
idades = []
soma = 0


for item in idadeTxt.split(","):
    item = item.strip() 

try:
    idades.append(int(item))
except ValueError:
    print(f"Valor '{item}' não é válido")
finally:
    idades.pop()
    for i in idades:
        soma += i
    print(f"A média é: {soma/len(idades)}")