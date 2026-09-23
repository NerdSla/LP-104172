import os
os.system('cls')

nome = str(input('Digite seu nome: '))
idade = int(input('Digite sua idade: '))

if idade < 16:
    print('Não podem votar.')
elif idade < 18:
    print('Voto opcional.')
elif idade <= 65:
    print('Voto obrigatório.')
else:
    print('Não é obrigado a votar.')