import os
os.system('cls')

soma = 0
contador = 0

while True:
    nota = float(input('Digite a nota desejada: '))
    esco = str(input('Deseja inserir mais uma nota (Y/N): ')).upper()
    if esco == 'Y':
        soma += nota
        contador = contador + 1
        os.system('cls')
        print(f'Contador: {contador}')
    elif esco == 'N':
        contador = contador + 1
        soma += nota
        media = soma / contador
        print(f'Média: {media}')
        break
    else:
        input('Alternativa Incorreta\nAperte qualquer botão para tentar novamente...')
        os.system('cls')