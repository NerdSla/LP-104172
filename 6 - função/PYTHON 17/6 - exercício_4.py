import os
os.system('cls')

def funcao_centimentro(metros):
    return metros * 100

metros = float(input(f'Quantos metros você quer transformar em centímetro: '))
centi = funcao_centimentro(metros)

print(f' {metros} metros são {centi} centimetros')