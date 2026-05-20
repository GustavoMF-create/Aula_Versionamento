#========================
# CALCULADORA EM PYTHON
#========================

def soma(a,b):
    return a + b

def multiplicacao(a,b):
    return a * b

def divisao(a,b):
    if b == 0:
        return "Div0"
    else:
        return a / b

def subtracao(a,b):
    return a - b

def exponenciacao(a,b):
    return a**b

def porcet(a,b):
    return(a*(b/100))


while True:
    print("\n======== Calculadora =========")   
    print("1-Soma")
    print("2-Multiplicação")
    print("3-Divisão")
    print("4-Subtração")
    print("5-Exponenciação")
    print("6-Porcentagem")
    print("0-Sair")
    
    opcao = int(input("Escolha o que deseja fazer: "))
    
    if opcao == 0:
        break
    
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    
    if opcao == 1:
        resultado = soma(num1,num2)
        print(f"Resultado = {resultado}")
    elif opcao == 2:
        resultado = multiplicacao(num1,num2)
        print(f"Resultado = {resultado}")
    elif opcao == 3:
        resultado = divisao(num1,num2)
        print(f"Resultado = {resultado}")
    elif opcao == 4:
        resultado = subtracao(num1,num2)
        print(f"Resultado = {resultado}")
    elif opcao == 5:
        resultado = exponenciacao(num1,num2)
        print(f"Resultado = {resultado}")
    elif opcao == 6:
        resultado = porcet(num1,num2)
        print(f"Resultado = {resultado}")

