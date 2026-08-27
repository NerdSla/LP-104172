import os
os.system('cls')

print('= SOLICITANDO DADOS =')
nome = str(input('Digite seu nome: '))
idade = int(input('Digite sua idade: '))
numero = float(input('Digite um número: '))

if numero < 10:
    print("É MENOR QUE 10!")

if numero > 10:
    print('É MAIOR QUE 10!')

if numero == 10:
    print('É IGUAL A 10!')