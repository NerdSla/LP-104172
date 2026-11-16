import os
from datetime import date
os.system('cls')

def idade(ano):
    idade = date.today().year - ano
    return idade

ano = int(input('Digite o ano de seu nascimento: '))

print(f'Você tem {idade(ano)} anos')