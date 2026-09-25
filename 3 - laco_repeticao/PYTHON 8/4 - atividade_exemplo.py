import os
os.system('cls')

print('ACUMULANDO VALORES EM UMA VARIÁVEL')
soma = 0

print(f'Valor da varável soma: {soma}')
num = int(input('Digite um número para soma: '))

for i in range(3):
    soma = soma + num
    print(f'Valor Temporario da variável soma: {soma}')

print(f'Valor final da variável soma: {soma}')