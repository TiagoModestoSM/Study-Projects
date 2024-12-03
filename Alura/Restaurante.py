import os
restaurantes = ['Pizza', 'Sushi']
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
    os.system('cls')
    print('Finalizando App\n')

def opcao_invalida():
    print('Opção Inválida')
    input('Digite uma tecla para voltar a tela inicial\n')
    main()

def cadastrar_novo_restaurante():
    os.system('cls')
    print('Cadastro de Novos restaurantes\n')
    nome_do_restaurante = input('Digite o Nome do Restaurante que deseja cadastrar: \n')
    restaurantes.append(nome_do_restaurante)
    print(f'O restaurante {nome_do_restaurante} foi cadastrado com sucesso')
    input('digite uma tecla para voltar ao menu principal ')
    main()

def listar_restaurantes():
    os.system('cls')
    print('Listando os restaurantes\n')
    for restaurante in restaurantes:
        print(f'.{restaurante}')

    input('\nDigite uma tecla para voltar ao menu principal ')
    main()

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