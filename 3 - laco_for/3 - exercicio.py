import os
os.system('cls')

print('= TABUADA =')
numero = int(input('Digite um número: '))
tabuada = input('Digite qual tabuada de 10 você quer ( + | - | * | / ): ')

match tabuada:
    case '+':
        for i in range(1, 11):
            print(f'{numero} + {i} = {numero + i}')
    case '-':
        for i in range(1, 11):
            print(f'{numero} - {i} = {numero - i}')
    case '*':
        for i in range(1, 11):
            print(f'{numero} * {i} = {numero * i}')
    case '/':
        for i in range(1, 11):
            print(f'{numero} / {i} = {numero / i}')
    case _:
        print('Tabuada inexistente')

print('FIM DO PROGRAMA.')