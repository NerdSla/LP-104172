import os
os.system('cls')

vetor_livros = []

for i in range(5):
    livro = input(f'Digite o {i + 1}º livro que deseja: ')
    vetor_livros.append(livro)

for i, livro in enumerate(vetor_livros):
    print(f'{i+1}º Livro: {livro}')