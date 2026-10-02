import os
os.system('cls')

while True:
    prim_nota = int(input('Digite sua primeira nota: '))
    seg_nota = int(input('Digite sua segunda nota: '))
    media = (prim_nota + seg_nota) / 2
    if prim_nota < 0 or prim_nota > 10 or seg_nota < 0 or seg_nota > 10:
        print('Dados incorretos.')
    else:
        print(f'Nota 1: {prim_nota}')
        print(f'Nota 2: {seg_nota}')
        print(f'Média: {media}')
        break