import os

lista_series = []
while True:
    os.system('cls')
    print('=== LISTA DAS SÉRIE ===\n1 - Adicionar Série\n2 - Listar Séries\n0 - Sair')
    opcao = input('Escolha uma opção: ')
    match opcao:
        case '1':
            print('\n== CADASTRAR SÉRIE ==')
            nome = input('Digite o nome da série: ').strip().upper()
            if nome == '':
                print('O nome não pode ficar vazio')
            elif nome in lista_series:
                print(f'{nome} já está cadastrado.')
            else:
                lista_series.append(nome)
                print('Série cadastrado com sucesso!')
            input('\nPressione uma tecla para continuar...')
        case '2':
            print('\n== LISTA DE SÉRIES ==')
            if len(lista_series) == 0:
                print('Não há nada na lista.')
            else:
                for i, série in enumerate(lista_series):
                    print(f'{i+1}ª Série: {série}')
                print(f'Total de séries: {len(lista_series)}')
            input('Pressione qualquer tecla para continuar...')
        case '0':
            print('Saindo do programa...')
            break
        case _:
            input('Opção Inválida\nAperte qualquer botão para voltar ao menu...')