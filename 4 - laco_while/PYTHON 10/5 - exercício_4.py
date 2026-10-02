import os
os.system('cls')

print('== Cadastro do Usuário ==')

log = input('Cadastre seu login: ')
sen = input('Cadastre sua senha: ')
tent = 0
lim_tent= 3
input('Cadastro Concluído! Agora pode logar')
os.system('cls')

while tent < lim_tent:
    log_sav = input('Digite seu login: ')
    sen_sav = input('Digite sua senha: ')
    if log_sav == log and sen_sav == sen:
        print('== Login Concluído! ==')
        break
    else:
        tent += 1
        tent_rest = lim_tent - tent
        if tent_rest > 0:
            input(f'== Login Inválido  ==\n Você tem {tent_rest} tentativas \n\n Tente novamente \n')
        else:
            print('Acesso Negado!')
            break
        os.system('cls')