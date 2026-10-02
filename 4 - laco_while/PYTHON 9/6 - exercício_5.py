import os
os.system('cls')

login_correto = "nerd"
senha_correta = "1234"
tentativas = 0
limite_tentativas = 3

while tentativas < limite_tentativas:
        login = input(f'Digite o login: ')
        senha = input(f'Digite a senha: ')
        
        if login == login_correto and senha == senha_correta:
            print('Bem-vindo!')
            break
        else:
            tentativas += 1
            tentativas_restantes = limite_tentativas - tentativas
            if tentativas_restantes > 0:
                print(f'\nLogin ou senha inválidos. Você ainda tem {tentativas_restantes} tentativa(s).\n')
            else:
                print('\nNúmero máximo de tentativas atingido. Acesso bloqueado!')
                input('aperte qualquer tecla pra continuar...')
                os.system('cls')