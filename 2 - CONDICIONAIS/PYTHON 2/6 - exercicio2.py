import os
os.system('cls')

print('= SOLICITANDO DADOS =')
nome = str(input('Digite seu nome: '))
idade = int(input('Digite sua idade: '))
primeira_nota = float(input('Digite a primeira nota: '))
segunda_nota = float(input('Digite a segunda nota: '))
terceira_nota = float(input('Digite sua terceira nota: '))

media = (primeira_nota + segunda_nota + terceira_nota) / 3

print('\n = EXIBINDO DADOS =')
print("Nome: ", nome)
print("Idade: ", idade)
print("Primeira nota: ", primeira_nota)
print("Segunda nota: ", segunda_nota)
print('Terceira nota: ', terceira_nota)
print("Média: ", media)

if media >= 7:
    print('APROVADO! :)')
else:
    print('REPROVADO! :(')