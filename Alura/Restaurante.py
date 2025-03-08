import os, datetime
from datetime import datetime
agora = datetime.now()
data_formatada = agora.strftime('%d/%m/%Y')
hora_formatada = agora.strftime('%H:%M:%S')

restaurantes = [{'nome': 'Pizzas', 'categoria': 'Pizza', 'ativo': True},
                {'nome': 'Sushis', 'categoria': 'Japonesa', 'ativo': False},
                {'nome': 'Comida', 'categoria': 'Italiana', 'ativo': False}]
def exibir_nome_do_programa():
    '''Essa função exibe o nome do programa na tela de comando'''
    print("""
█████████████████████▀███████████████████████████████████████████████████████████████
█─▄─▄─█▄─▄██▀▄─██─▄▄▄▄█▄─██─▄█▄─▄█▄─▀█▄─▄███─▄▄▄─█─▄▄─█▄─▀█▀─▄█▄─▄█▄─▄▄▀██▀▄─██─▄▄▄▄█
███─████─███─▀─██─██▄─██─██─███─███─█▄▀─████─███▀█─██─██─█▄█─███─███─██─██─▀─██▄▄▄▄─█
▀▀▄▄▄▀▀▄▄▄▀▄▄▀▄▄▀▄▄▄▄▄▀▀▄▄▄▄▀▀▄▄▄▀▄▄▄▀▀▄▄▀▀▀▄▄▄▄▄▀▄▄▄▄▀▄▄▄▀▄▄▄▀▄▄▄▀▄▄▄▄▀▀▄▄▀▄▄▀▄▄▄▄▄▀
""")
def exibir_opcoes():
    print('1. Cadastrar Restaurante')
    print('2. Listar Restaurante')
    print('3. Alterar estado do Restaurante')
    print('4. Sair\n')


def finalizar_app():
   exibir_subtitulo('Finalizando App')


def exibir_subtitulo(texto):
    os.system('cls')
    linha = '=' * (len(texto))
    print(linha)
    print(texto)
    print(linha)
    print()

def voltar_menu():
    
    input('\nDigite uma tecla para voltar ao menu principal: ')
    main()
    
def opcao_invalida():
    print('Opção Inválida')
    voltar_menu()


def cadastrar_novo_restaurante():
    exibir_subtitulo('Cadastro de Novos Restaurantes')
    nome_restaurante = input('Digite o Nome do Restaurante que deseja cadastrar: \n')
    categoria = input(f'Digite a categoria do restaurante {nome_restaurante}: ')
    dados_do_restaurante = {'nome': nome_restaurante, 'categoria': categoria, 'ativo': False}
    restaurantes.append(dados_do_restaurante)

    print(f'O restaurante {nome_restaurante} foi cadastrado com sucesso em {data_formatada} às {hora_formatada}')
    
    voltar_menu()

def listar_restaurantes():
    exibir_subtitulo('Listando os restaurantes')
    print(f'{'|NOME DO RESTAURANTE'.ljust(24)} | {'CATEGORIA'.ljust(20)} | {'STATUS'.ljust(20)}|')
    for i, restaurante in enumerate(restaurantes, start=1):
        nome_restaurante = restaurante['nome']
        categoria_restaurante = restaurante['categoria']
        ativos_restaurante = 'Ativado' if restaurante['ativo'] else 'Desativado'
        print(f'|{i}. {nome_restaurante.ljust(20)} | {categoria_restaurante.ljust(20)} | {ativos_restaurante.ljust(20)}|')
        
    voltar_menu()

def alterar_estado():
    exibir_subtitulo('Alterar estado do Restaurante')
    nome_do_restaurante = input('Digite o nome do restaurante que deseja ativar/desativar: ')
    restaurante_encontrado = False
    
    for restaurante in restaurantes:
        if nome_do_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            mensagem = f'O restaurante: {nome_do_restaurante} foi ativado com sucesso em {data_formatada} às {hora_formatada}' if restaurante['ativo'] else f' o {nome_do_restaurante} foi desativado com sucesso em {data_formatada} às {hora_formatada}'
            print(mensagem)
    if not restaurante_encontrado:
        print('Restaurante não encontrado')
    
    voltar_menu()
def escolher_opcoes():
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))
            
        if opcao_escolhida ==  1: # match opcao_escolhida:
         # case 1:
            cadastrar_novo_restaurante()
        elif opcao_escolhida ==  2:       #print('Adicionar restaurante')
            listar_restaurantes()
        elif opcao_escolhida ==  3:
            alterar_estado()
        elif opcao_escolhida == 4 :
            finalizar_app()
        else: # case _:print('Opção Inválida')
            opcao_invalida()
    except:
        opcao_invalida()
def main(): 
    os.system('cls')
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcoes()
    
if __name__ == '__main__':
    main()
