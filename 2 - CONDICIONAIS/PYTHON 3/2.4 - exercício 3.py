import os
os.system('cls')

nome = str(input('Digite seu nome: '))

primeiro_numero = float(input('Digite o primeiro número: '))
segundo_numero = float(input('Digite o segundo número: '))

print('= SOLICITANDO DADOS =')
maior = max(primeiro_numero, segundo_numero)
menor = min(primeiro_numero, segundo_numero)

print('\n = EXIBINDO DADOS =')
input(f'Primeiro número: {primeiro_numero}')
input(f'Segundo número: {segundo_numero}')
input(f'Maior: {maior}')
input(f'Menor: {menor}')