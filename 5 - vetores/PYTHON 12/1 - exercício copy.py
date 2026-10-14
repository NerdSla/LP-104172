import os
os.system('cls')

print('= INSERIDO NÚMEROS DO VETOR =')
vetor_numeros = []

for i in range(3):
    numero = int(input('Digite um número: '))
    vetor_numeros.append(numero)

print('\n= EXIBINDO NÚMEROS DO VETOR =')
for valor in vetor_numeros:
    print(f'Valor: {valor}')