import os

# Limpa o terminal.
os.system('cls')

print('= SOLICITANDO DADOS =')

nome = str(input('Digite seu nome: '))
idade = int(input('Digite sua idade '))
salario_funcionario = float(input('Digite seu salário: '))
salario_minimo = 1621.00

# CALCULANDO.

quantidades_de_salarios_minimos = salario_funcionario / salario_minimo

print('\n = EXIBINDO DADOS =')
print('Nome: ', nome)
print('Idade: ', idade)
print('Salário do Funcionário: ', salario_funcionario)
print('Salário Mínimo: ',salario_minimo)
print("Salário do Funcionário por Salário Mínimo ", quantidades_de_salarios_minimos)
print('ui ui quanto dinheiro')