import os
os.system('cls')

def par_impar(numero):
    if numero % 2 == 0:
        resultado = 'par'
    else:
        resultado = 'impar'
    return resultado

numero = float(input('Digite um número: '))
sol = par_impar(numero)

print(f'O número {numero} é {sol}')