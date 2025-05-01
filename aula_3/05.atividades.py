#Cada numeração corresponde a um programa diferente para que seja desenvolvido. As atividades seguem abaixo:

#1.Filtre produtos com preço > 1000 usando list comprehension;

lojavirtual = [
    {"nome": "Celular", "preco": 1500},
    {"nome": "Computador", "preco": 2000},
    {"nome": "Tablet", "preco": 1000},
    {"nome": "Drone", "preco": 2200}
]

def filtrar_produtos(preco_limite, operador):
    if operador == '>':
        return [produto for produto in lojavirtual if produto["preco"] > preco_limite]
    elif operador == '<=':
        return [produto for produto in lojavirtual if produto["preco"] <= preco_limite]

def menu():
    print("Escolha uma opção:")
    print("1 - Filtrar produtos acima de 1000")
    print("2 - Filtrar produtos abaixo ou igual a 1000")
    print("3 - Sair")

    opcao = input("Digite o número da opção desejada: ")
    return opcao

def main():
    while True:
        opcao = menu()
        
        if opcao == '1':
            produtos_acima_1000 = filtrar_produtos(1000, '>')
            print("Produtos acima de 1000:")
            for produto in produtos_acima_1000:
                print(f"{produto['nome']} - R${produto['preco']:.2f}")
        
        elif opcao == '2':
            produtos_abaixo_1000 = filtrar_produtos(1000, '<=')
            print("Produtos abaixo ou igual a 1000:")
            for produto in produtos_abaixo_1000:
                print(f"{produto['nome']} - R${produto['preco']:.2f}")

        elif opcao == '3':
            print("Saindo do programa...")
            break
        
        else:
            print("Opção inválida, tente novamente.")

main()

#2.Conte quantos produtos existem por categoria (usar dicionário);

#3.Remova duplicatas de uma lista de pedidos usando set.

#4.Uma empresa contratou seus serviços para armazenar dados de colaboradores em memória e realizar operações como:

#//Adicionar novos colaboradores.

def adicionar_colaborador(id, nome, salario):
    if id in colaboradores:
        print(f"Erro: colaborador com ID {id} já existe.")
        return
    colaboradores[id] = {"nome": nome, "salario": salario}
    print(f"Colaborador {nome} adicionado com sucesso.")

#//Buscar colaborador por ID.

    
}
    
    "id": 101,
    "nome": "Caio",
    "cargo": "Desenvolvedora Back-End"
} 

    "id": 101,
    "nome": "Mirella",
    "cargo": "Desenvolvedora de Python"
} 

    "id": 101,
    "nome": "Andressa",
    "cargo": "Analista de segurança"
} 


#//Listar colaboradores com salário acima de X.



'''
#Implemente utilizando funções.