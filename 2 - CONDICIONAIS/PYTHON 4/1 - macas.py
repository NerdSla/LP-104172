import os
os.system('cls')

# ENTRADA

print('= SOLICITANDO DADOS =')

nome = str(input('Digite seu nome: '))
quant_de_macas = int(input('Digite a quantidade de maçãs: '))

# PROCESSAMENTO

if quant_de_macas < 12:
    maca = quant_de_macas * 1.3
else:
    maca = quant_de_macas

# SAÍDA

print('\n = EXIBINDO DADOS =')

input(f'Valor total da compra: {maca:.2f}')