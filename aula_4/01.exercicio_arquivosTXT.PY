# Crie um programa que:
'''
Armazene usuários (nome, e-mail) em um arquivo.
Liste todos os usuários.
Permita excluir um usuário.
'''

with open('usuarios.txt', 'w') as dados:
    dados.write("Nome: Joao\nEmail: joaoluca@gmail\n")
    dados.write("Nome: Andressa\nEmail: Andressamotta@gmail\n")

with open('usuarios.txt' ,'r') as dados:
    conteudo = dados.read()
    print(conteudo)

import os
if os.path.exists('usuarios.txt'):
    os.remove('usuarios.txt')
    print("Arquivo removido!")
else:
    print("Arquivo não encontrado.")

    def listarUsuarios(nome_arquivo):
    '''Retorna o número de linhas de um arquivo.'''
    with open(nome_arquivo, 'r') as arquivo:
        return len(arquivo.readlines())
    