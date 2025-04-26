#// 1. Cálculo de Média de Notas: Peça ao usuário que insira 4 notas (de 0 a 10). Calcule a média das notas e exiba o resultado. Se a média for maior ou igual a 7, exiba "Aprovado". Caso contrário, exiba "Reprovado".

nota1 = float(input("Digite a primeira nota (0 a 10): "))
nota2 = float(input("Digite a segunda nota (0 a 10): "))
nota3 = float(input("Digite a terceira nota (0 a 10): "))
nota4 = float(input("Digite a quarta nota (0 a 10): "))

media = (nota1 + nota2 + nota3 + nota4) / 4

print("Média:", media)

if media >= 7:
    print("Aprovado")
else:
    print("Reprovado")

#//2. Soma dos Números Pares em um Intervalo: Peça ao usuário dois números, representando o início e o fim de um intervalo. Use um loop (for ou while) para calcular a soma de todos os números pares nesse intervalo e exiba o resultado.

inicio = int(input("Digite o número inicial do intervalo: "))
fim = int(input("Digite o número final do intervalo: "))

soma_pares = 0

for numero in range(inicio, fim + 1):
    if numero % 2 == 0:
        soma_pares += numero


        print("A soma dos números pares no intervalo é:", soma_pares)