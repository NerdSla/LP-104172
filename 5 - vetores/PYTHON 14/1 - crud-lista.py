import os

lista_produtos = []
while True:
  os.system('cls')
  # Menu do programa.
  print('''
=== MERCADINHO DENDEZEIROS ===
1 - Cadastrar produto
2 - Listar produtos
0 - Sair
''')
  opcao = input('Escolha uma opção: ')
  match opcao:
    case '1':
      print('\n== CADASTRAR UM PRODUTO ==')
      # strip() retira os espaços vazios no final.
      # upper() todas as letras maiúsculas.
      nome = input('Nome do produto: ').strip().upper()
      if nome == '':
        print('O nome não pode ficar vazio.')
      elif nome in lista_produtos:
        print(f'{nome} já está cadastrado.')
      else:
        # .append(nome) adiciona o nome do produto na lista.
        lista_produtos.append(nome)
        print('Produto cadastrado com sucesso!')
      input('\nPressione uma tecla para continuar...')
    case '2':
      print('\n== LISTA DOS PRODUTOS ==')
      # len(lista_produtos) mostra a quantidade de produtos.
      if len(lista_produtos) == 0:
        print('O estoque está vazio')
      else:
        for i, produto in enumerate(lista_produtos):
          print(f"{i+1}º Produto: {produto}")
        print(f'Total de produtos: {len(lista_produtos)}')
      input('Pressione ENTER para continuar...')
    case '0':
      print('Saindo do programa...')
      break
    case _:
      input('Opção Inválida\nAperte qualquer botão para voltar ao menu...')