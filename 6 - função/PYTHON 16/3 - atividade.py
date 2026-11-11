import os
os.system('cls')

# FAÇA UM PROGRAMA QUE SOLICITE:
# - NOME, EMAIL E TELEFONE
# O PROGRAMA DEVE MANTER NA TELA A LOGO:
# =================
#   SENAI - BAHIA
# =================
# A LOGO DEVE SER EXIBIDO USANDO FUNÇÃO:
#logo_senai()

# OS DADOS DEVERÃO SER APRESENTADOS POR MEIO
# DE UMA FUNÇÃO COM PARÂMETROS CHAMADA:
# mostrar_dados(nome, email, telefone)

def logo_senai():
    print('='*15)
    print(' SENAI - BAHIA')
    print('='*15)

def dados_resultados(nome, email, telefone):
    print(f'Nome: {nome}\nEmail: {email}\nTelefone: {telefone}')

logo_senai()
nome = input('Digite seu nome: ')

logo_senai()
email = input('Digite seu email: ')

logo_senai()
telefone = input('Digite seu telefone: ')

logo_senai()
dados_resultados(nome, email, telefone)