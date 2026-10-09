import os
os.system('cls')

grupo = 0
salario_grupo = 0
salario_mulher = 0
idademax = 0
idademin = 0

while True:
    menu = (input('Digite o número correspondente ao menu:\n1 | Adicionar pessoa\n2 | Exibir resultados \n3 | Sair\n'))
    match menu:
        case '1':
            usuario = input('Digite seu nome de usuário: ')
            idade = int(input('Digite a idade do usuário: '))
            sexo = input('Digite seu sexo ( M | F ): ').upper()
            if sexo == 'F':
                salariof = float(input('Digite seu sálario: R$ '))
                if salariof >= 5000:
                    salario_mulher = salario_mulher + 1
                grupo = grupo + 1
            else:
                salario = float(input('Digite seu sálario: R$ '))
                grupo = grupo + 1
                salario_grupo += salario
            if grupo == 1:
                idademax = idade
                idademin = idade
            else:
                idademax = max(idademax, idade)
                idademin = min(idademin, idade)
            os.system('cls')
        case '2':
            if grupo == 0:
                input('O grupo ainda não tem membros.\nPressione uma tecla para voltar ao menu...')
                os.system('cls')
            else:
                media = (salario_grupo + salariof) / grupo
                print(f'Média do Grupo: R$ {media}')
                print(f'Maior: {idademax}')
                print(f'Menor: {idademin}')
                print(f'Quantidades de mulheres com salário >= 5000: {salario_mulher}')
                input(f'Digite qualquer tecla para voltar ao menu...')
                os.system('cls')
        case '3':
            input('Digite qualquer tecla para SAIR do programa...')
            break