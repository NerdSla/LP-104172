import os
os.system('cls')

vetor_notas = []
soma = 0

for i in range(3):
    nota = float(input('Digite a sua nota: '))
    vetor_notas.append(nota)
    soma += nota

media = soma / 3
print(f'Média: {media}')
