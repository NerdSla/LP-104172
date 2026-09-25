import os
os.system('cls')

soma = 0

for i in range(4):
    soma += int(input('Digite um número para somar: '))

media = soma / 4

print(f'Média: {media}')