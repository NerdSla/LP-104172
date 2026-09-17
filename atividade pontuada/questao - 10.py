import os
os.system('cls')

print('Combustível | Quantidade Vendida | Desconto por Litro')
print('Álcool | Até 25 litros | 10%')
print('Álcool | Acima de 25 litros | 20%')
print('Gasolina | Até 25 litros | 15%')
print('Gasolina | Acima de 25 litros | 30%')
print('Gasolina = R$ 6.59 | Álcool = R$ 3.79')

alcool = 3.79
gasolina = 6.59

combustivel = input('Qual combustível você vai querer ( A - Álcool | G - Gasolina )? ')
quant_litros = float(input('Quantos litros você vai querer? '))

match combustivel:
    case 'A':
        valor = alcool * quant_litros
        if quant_litros <= 25:
            desconto = valor * 0.1
            print(f'Valor a ser pago: {valor - desconto}')
        else:
            desconto = valor * 0.2
            print(f'Valor a ser pago: {valor - desconto}')
    case 'G':
        valor = gasolina * quant_litros
        if quant_litros <= 25:
            desconto = valor * 0.15
            print(f'Valor a ser pago: {valor - desconto}')
        else:
            desconto = valor * 0.3
            print(f'Valor a ser pago: {valor - desconto}')