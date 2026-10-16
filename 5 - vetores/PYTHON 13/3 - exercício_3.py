import os
os.system('cls')

print('=== CARDÁPIO ===\nCódigo | Prato | Valor\n1 | Picanha | 25,00\n2 | Lasanha | 20,00\n3 | Strogonoff | 18,00\n4 | Bife Acebolado | 15,00\n5 | Pão com ovo | 5,00')
preco = 0
soma = 0
vetor_prato = []
vetor_preco = []
while True:
    prato = (input('Escolha o prato pelo código no cardápio: '))
    vetor_prato.append(prato)
    match prato:
        case '1':
            print('Picanha: R$ 25,00')
            preco = 25
            vetor_preco.append(preco)
        case '2':
            print('Lasanha: R$ 20,00')
            preco = 20
            vetor_preco.append(preco)
        case '3':
            print('Strogonoff: R$ 18,00')
            preco = 18
            vetor_preco.append(preco)
        case '4':
            print('Bife Acebolado: R$ 15,00')
            preco = 15
            vetor_preco.append(preco)
        case '5':
            print('Pão com ovo: R$ 5,00')
            preco = 5
            vetor_preco.append(preco)
    soma += preco
    escolha = str(input('Quer escolher outro prato( Y | N )? ')).upper()
    if escolha == 'Y':
        input('Clique em qualquer tecla para continuar...')
    elif escolha == 'N':
        os.system('cls')
        for i, prato in enumerate(vetor_prato):
            print(f'{i + 1}º prato: {prato}')
        print(f'Preço total: R$ {soma}')
        break
    else:
        print('Consideramos que você escolheu que Não.')
        for i, prato in enumerate(vetor_prato):
            print(f'{i + 1}º prato: {prato}')
        print(f'Preço total: R$ {soma}')
        break