import os
os.system('cls')

nome = str(input('Digite seu nome: '))
peso = float(input('Digite seu peso: '))
altura = float(input('Digite sua altura: '))

imc = peso / (altura * altura)

if imc < 18.5:
    print(f'IMC: {imc:.2f}, abaixo do peso')
elif imc < 25:
    print(f'IMC: {imc:.2f}, peso ideal (parabéns)')
elif imc < 30:
    print(f'IMC: {imc:.2f}, levemente acima do peso')
elif imc < 35:
    print(f'IMC: {imc:.2f}, obesidade grau I')
elif imc < 40:
    print(f'IMC: {imc:.2f}, obesidade grau II')
else:
    print(f'IMC: {imc:.2f}, obesidade grau III')