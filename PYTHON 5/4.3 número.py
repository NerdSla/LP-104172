import os
os.system('cls')

usuario = str(input('Digite seu usuário: '))
numero = float(input('Digite um número: '))

if numero >= 10 and numero <= 20:
    print(f'{numero} está no intervalo entre 10 e 20')