def somar(x, y):
    return x + y

def subtrair(x, y):
    return x - y

def multiplicar(x, y):
    return x * y

def dividir(x, y):
    if y == 0:
        return "Erro: divisão por zero"
    return x / y

print("Selecione a operação:")
print("1 - Somar")
print("2 - Subtrair")
print("3 - Multiplicar")
print("4 - Dividir")

escolha = input("Digite a opção (1/2/3/4): ")

try:
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))

    if escolha == '1':
        print("Resultado:", somar(num1, num2))
    elif escolha == '2':
        print("Resultado:", subtrair(num1, num2))
    elif escolha == '3':
        print("Resultado:", multiplicar(num1, num2))
    elif escolha == '4':
        print("Resultado:", dividir(num1, num2))
    else:
        print("Opção inválida.")
except ValueError:
    print("Erro: digite apenas números válidos.")