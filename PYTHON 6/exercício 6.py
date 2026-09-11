import os
os.system('cls')

altura = float(input('Qual a sua altura: '))
sexo = input('Qual o seu sexo(M/F): ')

match sexo:
    case 'M':
        peso_idealm = (72.7 * altura) - 58
        print(f'Seu peso ideal é: {peso_idealm}')
    case 'F':
        peso_idealf = (62.1 * altura) - 44.7
        print(f'Seu peso ideal é: {peso_idealf}')