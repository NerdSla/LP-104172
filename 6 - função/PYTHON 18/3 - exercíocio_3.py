import os
os.system('cls')

vetor_nota = []

def fun_media(vetor_nota):
    return sum(vetor_nota) / len(vetor_nota)

def fun_mos(media, vetor_nota):
    print('=== As notas ===')
    for nota in (vetor_nota):
        print(f'{i+1}ª Nota: {nota}')
    print(f'Média: {media}')

for i in range(3):
    nota = float(input(f'Digite a {i+1}ª nota: '))
    vetor_nota.append(nota)

media = fun_media(vetor_nota)

fun_mos(media, vetor_nota)