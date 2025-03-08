import os
restaurantes = [{'nome': 'Pizzas', 'categoria': 'Pizza', 'ativo': True},
                {'nome': 'Sushis', 'categoria': 'Japonesa', 'ativo': False},
                {'nome': 'Comida', 'categoria': 'Italiana', 'ativo': False}]
def exibir_nome_do_programa():
    print("""
█████████████████████▀███████████████████████████████████████████████████████████████
█─▄─▄─█▄─▄██▀▄─██─▄▄▄▄█▄─██─▄█▄─▄█▄─▀█▄─▄███─▄▄▄─█─▄▄─█▄─▀█▀─▄█▄─▄█▄─▄▄▀██▀▄─██─▄▄▄▄█
███─████─███─▀─██─██▄─██─██─███─███─█▄▀─████─███▀█─██─██─█▄█─███─███─██─██─▀─██▄▄▄▄─█
▀▀▄▄▄▀▀▄▄▄▀▄▄▀▄▄▀▄▄▄▄▄▀▀▄▄▄▄▀▀▄▄▄▀▄▄▄▀▀▄▄▀▀▀▄▄▄▄▄▀▄▄▄▄▀▄▄▄▀▄▄▄▀▄▄▄▀▄▄▄▄▀▀▄▄▀▄▄▀▄▄▄▄▄▀
""")
def exibir_opcoes():
    print('1. Cadastrar Restaurante')
    print('2. Listar Restaurante')
    print('3. Ativar Restaurante')
    print('4. Sair\n')


def finalizar_app():
   exibir_subtitulo('Finalizando App')


def exibir_subtitulo(texto):
    os.system('cls')
    print(texto)
    print()

def voltar_menu():
    
    input('\nDigite uma tecla para voltar ao menu principal: ')
    main()
    
def opcao_invalida():
    print('Opção Inválida')
    voltar_menu()


def cadastrar_novo_restaurante():
    exibir_subtitulo('Cadastro de Novos Restaurantes')
    nome_do_restaurante = input('Digite o Nome do Restaurante que deseja cadastrar: \n')
    categoria = input(f'Digite a categoria do restaurante {nome_do_restaurante}: ')
    dados_do_restaurante = {'nome': nome_do_restaurante, 'categoria': categoria, 'ativo': False}
    restaurantes.append(dados_do_restaurante)
    print(f'O restaurante {nome_do_restaurante} foi cadastrado com sucesso')
    voltar_menu()

def listar_restaurantes():
    exibir_subtitulo('Listando os restaurantes')
    for i, restaurante in enumerate(restaurantes, start=1):
        nome_restaurante = restaurante['nome']
        categoria_restaurante = restaurante['categoria']
        ativos_restaurante = restaurante['ativo']
        print(f'{i}. {nome_restaurante} | {categoria_restaurante} | {ativos_restaurante}')
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
            print('Ativar Restaurante')
        elif opcao_escolhida == 4 :
            finalizar_app()
        else: # case _:print('Opção Inválida')
            opcao_invalida()
    except:
        opcao_invalida()
def main(): 
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcoes()
    
if __name__ == '__main__':
    main()
