import os
os.system('cls')

while True:
    nota = int(input('Digite sua nota entre 1 e 10: '))
    if nota < 1 or nota > 10:
        print() # Pular uma linha
        print('Nota inválida, tente novamente!')
    else:
        print() # Assim como \n
        print(f'Nota: {nota}')
        break # Serve para parar o laço de repetição.

print('= FIM =')