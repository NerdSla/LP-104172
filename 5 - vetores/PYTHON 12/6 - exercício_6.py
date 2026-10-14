import os
os.system('cls')

vetor_numero = []
pares = 0
impares = 0

for i in range(6):
    numeros = float(input(f'Digite a {i + 1}ª nota que deseja: '))
    vetor_numero.append(numeros)
    if numeros % 2 == 0:
        pares = pares + 1
    else:
        impares = impares + 1

os.system('cls')

for i, numeros in enumerate(vetor_numero):
    print(f'{i+1}ª Nota: {numeros}')

print(f'Pares: {pares}')
print(f'Impares: {impares}')
