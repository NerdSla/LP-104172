import os
os.system('cls')

print('ACUMULANDO VALORES EM UMA VARIÁVEL')
soma = 0

for i in range(3):
    num = int(input('Digite um número para somar: '))
    soma = soma =+ num

print(f'Valor Final da variável soma: {soma}')