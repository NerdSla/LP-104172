import os
os.system('cls')

usuario = str(input('Digite seu usuário: '))
idade = int(input('Digite sua idade: '))
sexo = str(input('Digite seu sexo (M/F): '))
sexom = 'M'
sexof = 'F'

if sexo == sexom and idade >= 18:
    print('Você deve se apresentar ao serviço militar obrigatório.')
else:
    print('Você não deve apresentar-se ao serviço militar obrigatório.')