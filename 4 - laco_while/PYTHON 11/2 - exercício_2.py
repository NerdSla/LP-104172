import os
os.system('cls')

soma = 0
contador = 0

while True:
    nota = int(input('Digite um número inteiro: '))
    if nota >= 0:
        soma += nota
        contador = contador + 1
        print(f'Contador: {contador}')
    else:
        media = soma / contador
        print(f'Média: {media}')
        break