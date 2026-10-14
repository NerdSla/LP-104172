import os
os.system('cls')

vetor_notas = []

for i in range(3):
    notas = float(input(f'Digite a {i + 1}ª nota que deseja: '))
    vetor_notas.append(notas)

for i, notas in enumerate(vetor_notas):
    print(f'{i+1}ª Nota: {notas}')