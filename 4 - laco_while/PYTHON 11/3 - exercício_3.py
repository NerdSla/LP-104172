import os
os.system('cls')

soma = 0
contador = 0
pares = 0
impares = 0
soma_par = 0

while True:
    num_int = int(input('Digite um número inteiro positivo: '))
    if num_int >= 0:
        contador = contador + 1
        soma += num_int
        if num_int % 2 == 0:
            soma_par += num_int
            pares = pares + 1
        else:
            impares = impares + 1
    else:
        print(f'Pares: {pares}')
        print(f'Impares: {impares}')
        media = soma / contador
        media_pares = soma_par / pares
        print(f'Média Pares: {media_pares}')
        print(f'Média: {media}')
        break