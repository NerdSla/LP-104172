import os
os.system('cls')

nome = str(input('Digite seu nome: '))

primeira_nota = float(input('Digite o primeira nota: '))
segunda_nota = float(input('Digite o segunda nota: '))

media = (primeira_nota + segunda_nota) / 2

if media < 4:
    print(f'Média: {media}, Reprovado (E)')
elif media < 6:
    print(f'Média: {media}, Reprovado (D)')
elif media < 7.5:
    print(f'Média: {media}, Aprovado (C)')
elif media < 9:
    print(f'Média: {media}, Aprovado (B)')
else:
    print(f'Média: {media}, Aprovado (A)')