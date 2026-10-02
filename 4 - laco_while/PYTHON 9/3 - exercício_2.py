import os
os.system('cls')

while True:
    soma = 0
    for i in range(2):
        nota = int(input('Digite as notas que deseja: '))
        soma += nota
        media = (soma / 2)
        if nota < 1 or nota > 10:
            print('\n Nota inválida, tente novamente!')
    print(f'\n Media: {media}')
    break