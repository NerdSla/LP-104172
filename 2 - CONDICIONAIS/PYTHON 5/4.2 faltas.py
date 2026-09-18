import os
os.system('cls')

usuario = str(input('Digite seu usuário: '))
media = float(input('Digite sua média: '))
numero_faltas= int(input('Digite seu número de faltas: '))

if media >= 7 and numero_faltas <= 40:
    print('e o minin de papai e')
else:
    print('eae paen, tu ta onde?')