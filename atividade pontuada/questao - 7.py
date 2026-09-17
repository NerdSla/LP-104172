import os
os.system('cls')

nome = input('Digite o nome do produto: ')
quant_adquirida = int(input('Digite a quantidade adquirida: '))
preco_uni = float(input('Digite o preço unitário: '))
valor = preco_uni * quant_adquirida

if quant_adquirida <= 5:
    desconto = quant_adquirida * 0.02
elif quant_adquirida > 5 and quant_adquirida <= 10:
    desconto = quant_adquirida * 0.03
else:
    desconto = quant_adquirida * 0.05

print(f'Total a pagar: {valor - desconto}')