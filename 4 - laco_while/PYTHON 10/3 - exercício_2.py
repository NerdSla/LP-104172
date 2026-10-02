import os
os.system('cls')

m1 = 'Pão com Gelo: R$12.00'
m2 = 'Pão com Merda: R$20.00'
m3 = 'Pão com Gelo Gourmet: R$25.00'
m4 = 'Pão... NORMAL!: R$15.00'
m5 = 'Água com Mijo Gourmet: R$8.00'

print('Pão com Gelo = m1')
print('Pão com Merda = m2')
print('Pão com Gelo Gourmet = m3')
print('Pão... NORMAL! = m4')
print('Água com Mijo Gourmet = m5')

while True:
    menu = input('Digite a opção do menu ( m1 | m2 | m3 | m4 | m5 ): ').lower()
    match menu:
        case 'm1':
            print(f'{m1}')
            break
        case 'm2':
            print(f'{m2}')
            break
        case 'm3':
            print(f'{m3}')
            break
        case 'm4':
            print(f'{m4}')
            break
        case 'm5':
            print(f'{m5}')
            break
        case _:
            input('\n  Opção Inválida, Tente novamente!')
            os.system('cls')
