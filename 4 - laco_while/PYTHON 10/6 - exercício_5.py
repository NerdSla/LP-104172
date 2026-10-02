import os
os.system('cls')

soma = 0
QUANT_TENT = 3

for i in range (QUANT_TENT):
    while True:
        nota = int(input(f'Digite a {1+i}ª nota: '))
        if nota < 0 and nota > 10:
            input('Nota inválida \n Tente Novamente \n Pressione uma tecla para continuar...')
            os.system('cls')
        else:
            soma += nota
            break

media = soma / QUANT_TENT
if media < 5:
    print(f'Média: {media}: Você está reprovado')
elif media >= 5 and media <= 6.9:
    print(f'Média: {media}: Você está de Recuperação!')
else:
    print(f'Média: {media}: Aprovado!')