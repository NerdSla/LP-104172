import os
os.system('cls')

renda = float(input('Digite a sua renda mensal: '))
parcelas = int(input('Quantidade de parcelas: '))
emprestimo = int(input('Deseja quanto de emprestimo: '))

if parcelas != renda *10 and emprestimo <= (renda * 0.3):
    print('Não pode ser concedido')
else:
    print('Aprovado pelo banco')