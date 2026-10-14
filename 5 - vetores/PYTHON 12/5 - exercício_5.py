import os
os.system('cls')

vetor_notas = []

for i in range(4):
    notas = float(input(f'Digite a {i + 1}ª nota que deseja: '))
    vetor_notas.append(notas)

os.system('cls')
for i, notas in enumerate(vetor_notas):
    print(f'{i+1}ª Nota: {notas}')

min_vetor = min(vetor_notas)
max_vetor = max(vetor_notas)
print(f'Mínimo: {min_vetor}')
print(f'Máximo: {max_vetor}')