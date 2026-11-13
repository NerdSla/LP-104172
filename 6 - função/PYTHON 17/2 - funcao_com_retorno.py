import os
os.system('cls')

# Função com parâmetro e com retorno.
def calcular_notas(nota1, nota2):
    resultado = nota1 + nota2
    return resultado

print('= SOLICITANDO NOTAS =')
nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))

# Usando a função com parâmetros e com retorno.
soma = calcular_notas(nota1, nota2)

print('= EXIBINDO NOTAS =')
print(f'Soma = {soma}')


