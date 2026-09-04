import os
os.system('cls')

usuario = input('Digite seu usuário: ')
senha = input('Digite sua senha: ')
os.system('cls')

print(f'Usuário: {usuario}')
print(f'Senha: {senha}')

if usuario == 'NerdSla' and senha == '180508':
    print('Login concluído!')
else:
    print('Login falho.')