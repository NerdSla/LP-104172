import os
os.system('cls')

codigo = input('Digite o código do empregado: ')
ano_de_nascimento = int(input('Digite seu ano de nascimento: '))
tempo_trabalho = int(input('Digite o tempo de trabalho (em anos): '))
idade = 2026 - ano_de_nascimento
print(f'Código do empregado: {codigo}')
print(f'Idade: {idade}')
print(f'Tempo de trabalho: {tempo_trabalho} anos')
if idade >= 65 or tempo_trabalho >= 30:
    print('Requerer aposentadoria.')
else:
    print('Não requerer aposentadoria.')
