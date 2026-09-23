import os
os.system('cls')

picanha = 1
print('Picanha = 1')
lasanha = 2
print('Lasanha = 2')
strogonoff = 3
print('Strogonoff = 3')
bife_acebolado = 4
print('Bife Acebolado = 4')
pao_com_ovo = 5
print('Pão com ovo = 5')

prato = input('Digite o número que o prato escolhido: ')

match prato:
    case "1":
        print("Picanha: 25R$.")
    case "2":
        print("Lasanha: 20R$.")
    case "3":
        print("Strogonoff: 18R$.")
    case "4":
        print("Bife Acebolado: 15R$.")
    case "5":
        print("Pão com ovo: 5R$.")
    case _:
        print("Prato inválido.")
