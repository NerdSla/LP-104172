import os
os.system('cls')

verde = 10.00
azul = 20.00
amarelo = 30.00
vermelho = 40.00

cor = str(input('Digite o CD que deseja baseado na cor marcada ( verde | azul | amarelo | vermelho ): ')).lower()

match cor:
    case 'verde':
        print(f'Preço: R$ {verde}')
    case 'azul':
        print(f'Preço: R$ {azul}')
    case 'amarelo':
        print(f'Preço: R$ {amarelo}')
    case 'vermelho':
        print(f'Preço: R$ {vermelho}')