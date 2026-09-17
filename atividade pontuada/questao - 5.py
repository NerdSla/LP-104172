import os
os.system('cls')

a = int(input('Digite o primeiro número: '))
b = int(input('Digite o segundo número: '))
operacao = input('Digite a operação que deseja ( + | - | * | / ): ')

match operacao:
    case '+':
        soma = a + b
        print(f'Soma: {soma}')
    case '-':
        subtracao = a - b
        print(f'Subtração: {subtracao}')
    case '*':
        multiplicacao = a * b
        print(f'Multiplicação: {multiplicacao}')
    case '/':
        divisao = a / b
        print(f'Divisão: {divisao}')