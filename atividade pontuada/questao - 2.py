import os
os.system('cls')

nome = input('Digite seu nome: ')
sexo = str(input('Digite seu sexo (M/F): ')).lower()
estado_civil = str(input('Digite seu estado civil: ')).lower()

print(f'Nome: {nome}')
print(f'Sexo: {sexo}')
print(f'Estado Civil: {estado_civil}')

if estado_civil == 'casada' and sexo == 'f':
    tempo_de_casada = int(input('Digite seu tempo de casada: '))
    print(f'Tempo de casada: {tempo_de_casada}')