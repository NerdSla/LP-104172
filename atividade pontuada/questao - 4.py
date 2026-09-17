import os
os.system('cls')

print('Fruta | Até 5 kg | Acima de 5 kg')
print('Morango | R$ 2.5 por kg | R$ 2.2 por kg')
print('Morango | R$ 1.8 por kg | R$ 1.5 por kg')

quant_morango = int(input('Quantos quilos (Kg) você quer comprar de morango? '))
quant_maca = int(input('Quantos quilos (Kg) você quer comprar de maçã? '))

if quant_morango < 5:
    morango = 2.5
else:
    morango = 2.2

if quant_maca < 5:
    maca = 1.8
else:
    maca = 1.5

valor = (morango * quant_morango) + (maca * quant_maca)
desconto = valor * 0.1

print(f'Quantidade de Morangos (em Kg): {quant_morango}')
print(f'Quantidade de Maçãs (em Kg): {quant_maca}')

if (quant_maca + quant_morango) == 10 or valor == 15:
    print(f'Valor a ser pago: {valor - desconto}')
else:
    print(f'Valor a ser pago: R$ {valor}')