import os
os.system('cls')

domingo = 1
print('Domingo = 1')
segunda = 2
print('Segunda = 2')
terca = 3
print('Terça = 3')
quarta = 4
print('Quarta = 4')
quinta = 5
print('Quinta = 5')
sexta = 6
print('Sexta = 6')
sabado = 7
print('Sábado = 7')
dia = int(input('Digite o número que represente o dia da semana: '))

match dia:
    case 2 | 3 | 4 | 5 | 6:
        print('Dia útil')
    case 1 | 7:
        print('Final de Semana')
    case _:
        print('Dia inválido')