import os
os.system('cls')

valor = float(input('Digite o valor do produto: '))
forma_pag = input('Digite a forma de pagamento (1/2): ')
pagamento_vista = 1
pagamento_prazo = 2
desconto = valor * 0.1
match forma_pag:
    case '1':
        print(f'Valor do produto: {valor}')
        print('Forma de pagamento: à vista')
        print(f'Valor do desconto: {desconto}')
        print(f'Total a pagar: {valor - desconto}')
    case '2':
        print(f'Valor: {valor}')
        quant_parcelas = int(input('Digite a quantidade de parcelas (1 à 6): '))
        parcela = valor / quant_parcelas
        print(f'Valor do produto: {valor}')
        print('Forma de pagamento: à prazo')
        print(f'Quantidade de parcelas: {quant_parcelas}')
        print(f'Valor por parcela: {parcela}')
        print(f'Total a prazo: {valor}')
