import os

# Limpa o terminal.
os.system("cls")

# SOLICITANDO DADOS
# input adiciona o que for digitado no terminal na variável como texto.
nome = input("Digite seu nome: ")
sobrenome = input("Digite o seu sobrenome: ")

# int() converte o que foi digitado em inteiro (números inteiros).
idade = int(input("Digite sua idade: "))

# float() converte o que foi digitado em float (número reais)
peso = float(input("Digite sua peso: "))
altura = float(input("Digite sua altura: "))

# MOSTRANDO DADOS.
print("Nome: ", nome)
print("Sobrenome: ", sobrenome)
print("Idade: ", idade)
print("Peso: ", peso)
print("Altura: ", altura)