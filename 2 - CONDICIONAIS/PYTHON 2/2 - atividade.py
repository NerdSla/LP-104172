import os

# Limpa o terminal.
os.system('cls')

print('= SOLICITANDO DADOS =')
nome = str(input('Digite seu nome: '))
idade = int(input('Digite sua idade: '))
primeiro_numero = float(input('Digite o primeiro número: '))
segundo_numero = float(input('Digite o segundo número: '))

# CALCULANDO.

soma = primeiro_numero + segundo_numero
subtracao = primeiro_numero - segundo_numero
multiplicacao = primeiro_numero * segundo_numero
divisao = primeiro_numero / segundo_numero

print('\n = EXIBINDO DADOS =')
print("Nome: ", nome)
print("Idade: ", idade)
print("Primeiro número: ", primeiro_numero)
print("Segundo número: ", segundo_numero)
print("Soma: ", soma)
print('Subtração: ', subtracao)
print('Multiplicação: ', multiplicacao)
print('Divisão: ', divisao)
print('uhuuu matemática uhuuu')