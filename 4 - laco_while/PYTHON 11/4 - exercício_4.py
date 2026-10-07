import os
os.system('cls')

soma = 0
contador = 0
grupo = 0
salario_grupo = 0
salario_mulher = 0

while True:
    menu = (input('Digite o número correspondente ao menu:\n1 | Adicionar pessoa\n2 | Exibir resultados \n3 | Sair'))
    match menu:
        case '1':
            usuario = input('Digite seu nome de usuário: ')
            idade = int(input('Digite a idade do usuário: '))
            sexo = input('Digite seu sexo ( M | F ): ').upper()
            if sexo == 'F':
                salariof = float('Digite seu sálario: R$ ')
                if salariof >= 5000:
                    salario_mulher = salario_mulher + 1
            else:
                salario = float(input('Digite seu sálario: R$ '))
            grupo = grupo + 1
            salario_grupo += salario
            os.system('cls')
        case '2':
            media = (salario_grupo + salario_grupo)