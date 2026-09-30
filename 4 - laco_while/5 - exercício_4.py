import os
os.system('cls')

while True:
    login = str(input('Digite seu login: '))
    senha = int(input('Digite sua senha: '))
    if login == 'NerdSla' and senha == 1234:
        print(f'Login: {login}')
        print(f'Senha: {senha}')
        print('FIM')
        break
    else:
        print('\n Login inválido')
        input('Pressione uma tecla para continuar...')
        os.system('cls')