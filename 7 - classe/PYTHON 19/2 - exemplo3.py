from dataclasses import dataclass
import os
os.system('cls')


@dataclass
class Cliente:
    # Nome da variável : tipo da variável
    nome: str
    idade: int
    altura: float
    peso: float

lista_clientes = []

print('SOLICITANDO DADOS DE DOIS CLIENTE')
for i in range(2):
    dados_do_cliente = Cliente(
        nome = input('\nDigite o nome do cliente: '),
        idade = int(input('Digite sua idade: ')),
        altura = float(input('Digite sua altura: ')),
        peso = float(input('Digite seu peso em kg: '))
    )
    lista_clientes.append(dados_do_cliente)

print('\nEXIBINDO DADOS')
for cliente in lista_clientes:
    print(f'Nome: {cliente.nome}')
    print(f'Idade: {cliente.idade}')
    print(f'Altura: {cliente.altura}')
    print(f'Peso: {cliente.peso}')
    print('='*15)