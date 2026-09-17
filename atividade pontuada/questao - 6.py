import os
os.system('cls')

a = float(input('Digite a primeira nota: '))
b = float(input('Digite a segunda nota: '))

media = (a + b) / 2

print(f'Nota: {media}')

if media > 6:
    print('Parabéns, você está aprovado!')
elif media >= 4.1 and media <= 5.9:
    print('Você está de recuperação!')
else:
    print('Reprovado!')