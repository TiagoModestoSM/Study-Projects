import os, datetime, random
from datetime import datetime
from modelos.restaurante_final import Restaurante
from modelos.cardapio.bebida import Bebida
from modelos.cardapio.prato import Prato
from assests.exibir_subtitulo import exibir_subtitulo
from assests.exibir_nome_do_programa import exibir_nome_do_programa


def escolher_opcoes():
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))
        
        if opcao_escolhida == 1:
            os.system('cls')
            exibir_subtitulo('CADASTRO DE NOVOS RESTAURANTES')
            Restaurante.cadastrar_novo_restaurante()
        elif opcao_escolhida == 2:
            os.system('cls')
            exibir_subtitulo('LISTA DE RESTAURANTES')
            Restaurante.listar_restaurantes()
        elif opcao_escolhida == 3:
            Restaurante.alternar_estado()
        elif opcao_escolhida == 5:
            finalizar_app()
        else:
            opcao_invalida()
    except:
        opcao_invalida()
            
            
def opcao_invalida():
    print('Opção Inválida')
    voltar_menu()
    
def voltar_menu():
    
    input('\nDigite uma tecla para voltar ao menu principal: ')
    main()
    
    
def finalizar_app():
   exibir_subtitulo('Finalizando App')
   exit
    
def main():
    os.system('cls')
    exibir_nome_do_programa()
    Restaurante.exibir_opcoes()
    escolher_opcoes()

if __name__ == '__main__':
    main()  
