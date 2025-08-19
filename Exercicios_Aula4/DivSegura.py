n1 = (input("Digite um numero: "))
n2 = (input("Digite um numero: "))

try:
    print(f"{int(n1)/int(n2)}")
except ZeroDivisionError:
    print(f"O segundo valor é zero")
except ValueError:
    if(type(n1) != type(int)):
        print(f"Você não digitou um numero no primeiro")
    elif(type(n2) != type(int)):
        print(f"Você não digitou um numero no segundo")
    else:
        print(f"Você não digitou nenhum número")
finally:
    print(f"Operação encerrada!")