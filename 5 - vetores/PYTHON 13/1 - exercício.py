import os
os.system('cls')

vetor_numero = []
vetor_neg = []
soma = 0

for i in range(5):
    numero = int(input(f'Digite {i + 1}º número: '))
    vetor_numero.append(numero)
    if numero < 0:
        num_neg = numero
        vetor_neg.append(num_neg)
    else:
        soma += numero

os.system('cls')

for i, num_neg in enumerate(vetor_neg):
    print(f'{i + 1}º número negativo: {num_neg}')

print(f'Soma dos positivos: {soma}')