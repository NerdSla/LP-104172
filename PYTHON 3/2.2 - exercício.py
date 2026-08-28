import os
os.system('cls')

nome = str(input('Digite seu nome: '))

primeiro_numero = float(input('Digite o primeiro número: '))
segundo_numero = float(input('Digite o segundo número: '))

print('= SOLICITANDO DADOS =')
media = (primeiro_numero + segundo_numero) / 2
soma = primeiro_numero + segundo_numero
produto = primeiro_numero * segundo_numero
maior = max(primeiro_numero, segundo_numero)
menor = min(primeiro_numero, segundo_numero)

print('\n = EXIBINDO DADOS =')
input(f'Média: {media}')
input(f'Soma: {soma}')
input(f'Produto: {produto}')
input(f'Maior: {maior}')
input(f'Menor: {menor}')

if primeiro_numero == segundo_numero:
    input('Os números são iguais')
else:
    input('Os números são diferentes')