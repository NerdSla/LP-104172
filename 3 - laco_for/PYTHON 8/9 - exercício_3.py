import os
os.system('cls')

nota = 0

for i in range(3):
    nota += int(input('Digite um número para somar: '))

media = nota / 3
print(f'Media: {media}')

if media >= 7:
    print('Aprovado!')
elif media < 4:
    print('Reprovado')
else:
    print('Recuperação')