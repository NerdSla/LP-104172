import os
os.system('cls')

a = int(input('Digite o primeiro número: '))
b = int(input('Digite o segundo número: '))
c = int(input('Digite o terceiro número: '))

soma = a + b

if soma < c:
    print('A soma de A + B é menor que C')
else:
    print('A soma de A + B é maior que C')