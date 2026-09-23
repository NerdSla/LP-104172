import os
os.system('cls')

num1 = float(input('Digite o primeiro número: '))
num2 = float(input('Digite o segundo número: '))
operador = input('Digite a operação desejada( + | - | * | / ): ')

soma = num1 + num2
subtracao = num1 - num2
multiplicacao = num1 * num2
divisao = num1 / num2

match operador:
    case '+':
        print(f'Operador: soma, {soma}')
    case '-':
        print(f'Operador: subtracão, {subtracao}')
    case '*':
        print(f'Operador: multiplicação, {multiplicacao}')
    case '/':
        print(f'Operador: divisão, {divisao}')
    case _:
        print(f'Operação inválida.')