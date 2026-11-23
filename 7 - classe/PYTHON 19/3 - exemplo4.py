from dataclasses import dataclass
import os
os.system('cls')

# CRIE UMA CLASSE PARA OS DADOS DE UM CLIENTE.
# DADOS: NOME, TELEFONE E E-MAIL.

@dataclass
class Cliente:
    nome: str
    telefone: str
    email: str

lista_clientes = []

for i in range(2):
    dados_do_cliente = Cliente(
        nome = input('\nDigite o nome do cliente: '),
        telefone = input('Digite seu telefone sem símbolos ou sinais: '),
        email = input('Digite seu email: '),
    )
    lista_clientes.append(dados_do_cliente)

for cliente in lista_clientes:
    print(f'Nome: {cliente.nome}')
    print(f'Telefone: {cliente.telefone}')
    print(f'Email: {cliente.email}')
    print('='*15)