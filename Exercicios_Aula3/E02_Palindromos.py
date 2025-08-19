palavra = str(input("Digite uma palavra: ")).strip()
palavraReverse = palavra[::-1]

print(palavraReverse)

if(palavra == palavraReverse):
    print("É palindromo")
else:
    print("Não é")