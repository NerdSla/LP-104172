import os
os.system('cls')

print('= SOLICITANDO DADOS =')
nome = str(input('Digite seu nome: '))
idade = int(input('Digite sua idade: '))
primeiro_numero = float(input('Digite a primeiro número: '))
segundo_numero = float(input('Digite a segunda número: '))
media = (primeiro_numero + segundo_numero) / 2
soma = primeiro_numero + segundo_numero
produto = primeiro_numero * segundo_numero
maior = max(primeiro_numero, segundo_numero)
menor = min(primeiro_numero, segundo_numero)

print('\n = EXIBINDO DADOS =')
print(f'Nome: {nome}')
print(f'Idade: {idade}')
print(f'Primeiro Número: {primeiro_numero}')
print(f'Segundo Número: {segundo_numero}')
print(f'Média: {media}')
print(f'Soma: {soma}')
print(f'Produto: {produto}')
print(f'Maior: {maior}')
print(f'Menor: {menor}')