import os
os.system('cls')

soma = 0
QUANTIDADE_NOTAS = 2

for i in range(QUANTIDADE_NOTAS):
    while True:
        nota = float(input(f'Digite a {1+i}ª nota entre 0 e 10: '))
        if nota < 0 or nota > 10:
            print('Nota inválida \n Tente novamente \n')
            input('Pressione uma tecla para continuar...')
            os.system('cls')
        else:
            soma += nota
            break

media = soma / QUANTIDADE_NOTAS
print(f'Média: {media}')
