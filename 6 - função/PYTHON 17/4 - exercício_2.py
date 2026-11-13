import os
os.system('cls')

def pos_neg(numero):
    if numero > 0:
        resultado = 'Positivo'
    elif numero == 0:
        resultado = 'Neutro'
    else:
        resultado = 'Negativo'
    return resultado

numero = int(input('Digite um número: '))
resultado = pos_neg(numero)

print(f'Esse número é... {resultado}')