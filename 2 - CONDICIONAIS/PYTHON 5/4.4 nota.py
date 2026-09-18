import os
os.system('cls')

usuario = str(input('Digite seu usuário: '))
nota = float(input('Digite um nota: '))

if nota >= 0 and nota <= 10:
    print(f'Nota: {nota}')
else:
    print('Nota deve estar entre 0 e 10')