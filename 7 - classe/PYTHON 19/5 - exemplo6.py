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
    
    # Função dentro da classe.
    def mostrar_dados(self):
        print(f'Nome: {self.nome}')
        print(f'Telefone: {self.telefone}')
        print(f'E-mail: {self.email}')
        print('='*30)
    
    # Função somente para enviar e-mails.
    def email_marketing(self):
        print(f'Nome: {self.nome}')
        print(f'Telefone: {self.telefone}')
        print(f'E-mail: {self.email}')
        print('='*30)

lista_clientes = []

print('\n= SOLICITANDO DADOS =')
for i in range(2):
    dados = Cliente(
        nome = input('\nDigite o nome do cliente: '),
        telefone = input('Digite seu telefone sem símbolos ou sinais: '),
        email = input('Digite seu email: '),
    )
    lista_clientes.append(dados)

print('\n= EXIBINDO DADOS =')
for cliente in lista_clientes:
    cliente.mostrar_dados()
for cliente in lista_clientes:
    print('\n EXIBINDO E-MAIL MARKETING =')
    cliente.email_marketing()
