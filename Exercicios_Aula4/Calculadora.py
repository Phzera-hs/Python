class OperadorInvalido(Exception):  
    pass    

def ContaExcept(num1,num2):
    operador = input("Digite o operador: (+,-,*,/)")
    conta = None
    try:
        print()
        if(operador == '+'):
            conta = num1 + num2
        elif(operador == '-'):
            conta = num1 - num2
        elif(operador == '*'):
            conta = num1 * num2
        elif(operador == '/'):
            conta = num1 / num2
        else:
            raise OperadorInvalido()
    except OperadorInvalido:
        print(f"Operador {operador} inválido: ")
    finally:
        print(conta)

ContaExcept(1,2)
        
        


