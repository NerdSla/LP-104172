import os
os.system('cls')

# Função com parâmetro e com retorno.
def calcular_notas(nota1, nota2):
    resultado = nota1 + nota2
    return resultado

def calcular_media(nota1, nota2):
    resultado = soma / 2
    return resultado

def aprovado_reprovado(media):
    if media >= 7:
        resultado = 'Aprovado!'
    else:
        resultado = 'Reprovado'
    return resultado

print('= SOLICITANDO NOTAS =')
nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))

# Usando a função com parâmetros e com retorno.
soma = calcular_notas(nota1, nota2)
media = calcular_media(nota1, nota2)
situacao = aprovado_reprovado(media)

print('= EXIBINDO NOTAS =')
print(f'Soma = {soma}')
print(f'Média = {media}')
print(f'{situacao}')