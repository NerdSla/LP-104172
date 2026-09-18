import os

# Limpa o terminal.
os.system('cls')

print('= SOLICITANDO DADOS =')
nome = input('Digite seu nome: ')
idade = int(input('Digite sua idade: '))
valor = int(input('Digite o valor: '))

# CALCULANDO.

antecessor = valor - 1
sucessor = valor + 1

print('\n = EXIBINDO DADOS =')
print("Nome: ", nome)
print("Idade: ", idade)
print("Valor: ", valor)
print("Antecessor: ", antecessor)
print("Sucessor: ", sucessor)