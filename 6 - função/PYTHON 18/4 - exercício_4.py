import os
os.system('cls')

notas = []

def fun_media(notas):
    return sum(notas) / len(notas)

def mostrar(media):
    print(f'Média: {media}')
    if media < 7:
        print('Reprovado')
    else:
        print('Aprovado')

for i in range(2):
    while True:
        nota = float(input('Digite uma nota (0-10): '))
        if nota >= 0 and nota <= 10:
            notas.append(nota)
            break
        else:
            print('Número inválido')

media = fun_media(notas)
mostrar(media)