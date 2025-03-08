import os

pessoa = [{'nome': '', 'idade': '', 'cidade': ''}]

nome = input('Digite seu nome: ')
idade = input('Digite sua idade: ')
cidade = input('Digite sua cidade: ')
dados_da_pessoa = [{'nome': nome, 'idade': idade, 'cidade': cidade}]
pessoa.append(dados_da_pessoa)




print(f'Olá, me chamo {nome}, tenho {idade} anos e sou de {cidade}')