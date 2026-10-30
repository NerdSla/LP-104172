import os

lista_paciente = []
while True:
    os.system('cls')
    # Menu do programa.
    print('''
    === HOSPITAL ===
    1 - Cadastrar paciente
    2 - Listar pacientes
    3 - Atualizar paciente
    4 - Remover paciente
    5 - Buscar paciente
    0 - Sair
    ''')
    opcao = input('Escolha uma opção: ')
    match opcao:
        case '1':
            # CREATE (CRIAR)
            print('\n== CADASTRAR UM PACIENTE ==')
            nome = input('Nome do paciente: ').strip().upper()
            sobre = input('Sobrenome do paciente: ').strip().upper()
            if nome == '' or sobre == '':
                print('O nome e o sobrenome não podem ficar vazio.')
            elif nome and sobre in lista_paciente:
                print(f'{nome} {sobre} já está cadastrado.')
            else:
                lista_paciente.append(nome)
                lista_paciente.append(sobre)
                print('Paciente cadastrado com sucesso!')
            input('\nPressione uma tecla para continuar...')
        case '2':
            # READ (LER / CONSULTAR / BUSCAR)
            print('\n== LISTA DOS PRODUTOS ==')
            if len(lista_paciente) == 0:
                print('O estoque está vazio')
            else:
                for i, paciente in enumerate(lista_paciente):
                    print(f"{i+1}º Paciente: {paciente}")
                print(f'Total de Paciente: {len(lista_paciente)}')
            input('\nPressione uma tecla para continuar...')
        case '3':
            # UPDATE (ATUALIZAR)
            print('== ATUALIZAR PRODUTO ==')
            print('1 - Nome\n2 - Sobrenome')
            opcao = input('Digite uma opção: ')
            match opcao:
                case '1':
                    nome = input('Qual o produto deseja atualizar? ').strip().upper()
                    if nome in lista_paciente:
                        posicao = lista_paciente.index(nome)
                        novo = input('Novo nome: ').strip().upper()
                        lista_paciente[posicao] = novo
                        print('Nome do paciente alterado com sucesso!')
                    else:
                        print('Paciente não encontrado.')
                    input('\nPressione uma tecla para continuar...')
                case '2':
                    a
                case '4':
                    # REMOVE/DELETE (REMOVER / DELETAR)
                    print('== REMOVER PRODUTO ==')
                    nome = input('Qual produto deseja remover? ').strip().upper()
                    if nome in lista_paciente:
                        lista_paciente.remove(nome)
                        print('Produto removido com sucesso!')
                    else:
                        print('Produto não encontrado.')
                    input('\nPressione uma tecla para continuar...')
                case '5':
                    # READ (LER / CONSULTAR / BUSCAR)
                    print('== BUSCAR PRODUTO ==')
                    nome = input('Qual produto deseja buscar? ').strip().upper()
                    if nome in lista_paciente:
                        print('Produto encontrado!')
                    else:
                        print('Este produto não está no estoque.')
                    input('\nPressione uma tecla para continuar...')
                case '0':
                    print('Saindo do programa...')
                    break
                case _:
                    input('Opção Inválida\nAperte qualquer botão para voltar ao menu...')