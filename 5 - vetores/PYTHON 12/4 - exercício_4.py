import os
os.system('cls')

vetor_notas = []
soma = 0

for i in range(4):
    notas = float(input(f'Digite a {i + 1}ª nota que deseja: '))
    vetor_notas.append(notas)
    soma += notas

os.system('cls')

for i, notas in enumerate(vetor_notas):
    print(f'{i+1}ª Nota: {notas}')
media = soma / 4
print(f'Média: {media}')

if media < 5:
    print('Reprovação')
elif media >= 7:
    print('Aprovado!')
else:
    print('Recuperação')