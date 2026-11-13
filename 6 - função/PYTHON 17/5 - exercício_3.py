import os
os.system('cls')

def mais(num1, num2):
    resultado = num1 + num2
    return resultado

def menos(num1, num2):
    resultado = num1 - num2
    return resultado

def vezes(num1, num2):
    resultado = num1 * num2
    return resultado

def div(num1, num2):
    if num2 == 0:
        print('Não é possivel dividir por zero')
        num2 = 1
    resultado = num1 / num2
    return resultado

num1 = float(input('Digite o primeiro número: '))
num2 = float(input('Digite o segundo número: '))
soma = mais(num1, num2)
subt = menos(num1, num2)
mult = vezes(num1, num2)
divi = div(num1, num2)

print(f'Soma: {soma}')
print(f'Subtração: {subt}')
print(f'Multiplicação: {mult}')
print(f'Divisão: {divi}')



