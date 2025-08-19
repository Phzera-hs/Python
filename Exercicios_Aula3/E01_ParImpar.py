numeros = []
par = []
impar = []
soma = 0

while True:
    num = int(input("Digite um valor: "))
    if(num == 0):
        break
    if(num % 2 == 0):
        numeros.append(num)
        par.append(num)
    else:
        numeros.append(num)
        impar.append(num)

maior = numeros[0]
menor = numeros[0]

for i in numeros:
    soma += i
    media = soma/len(numeros)

print(f"Media = {media}")

for numero in numeros:
    if(maior < numero):
        maior = numero
    if(menor > numero):
        menor = numero


print(f"Maior = {maior}")
print(f"Menor = {menor}")