import os
os.system('cls')

def inflacao(preco):
    if preco < 100:
        preco = preco + (preco * 0.1)
    else:
        preco = preco + (preco * 0.2)
    return preco

preco = float(input('Digite o preço do protudo: R$ '))

print(f'Preço total: R$ {inflacao(preco)}')