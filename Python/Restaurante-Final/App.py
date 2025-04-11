import os, datetime, random, sys
from datetime import datetime
from modelos.restaurante_final import Restaurante
from modelos.cardapio.bebida import Bebida
from modelos.cardapio.prato import Prato
import utils.helpers as he
from PyQt5.QtWidgets import QApplication, QWidget
from assets import botton


def exibir_opcoes():
    print('1. Cadastrar Restaurante')
    print('2. Listar Restaurante')
    print('3. Alterar Estado do Restaurante')
    print('4. Remover Restaurante')
    print('5. Mandar Avaliação')
    print('6. Sair')

def escolher_opcoes():
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))
        
        if opcao_escolhida == 1:
            he.exibir_subtitulo('CADASTRO DE NOVOS RESTAURANTES')
            Restaurante.cadastrar_novo_restaurante()
            he.voltar_menu()
        elif opcao_escolhida == 2:
            he.exibir_subtitulo('LISTA DE RESTAURANTES')
            listar_restaurante()
            he.voltar_menu()
        elif opcao_escolhida == 3:
            he.exibir_subtitulo('ALTERNAR ESTADO DO RESTAURANTE')
            listar_restaurante()
            Restaurante.alternar_estado()
            he.voltar_menu()
        elif opcao_escolhida == 4:
            he.exibir_subtitulo('REMOVER RESTAURANTE')
            listar_restaurante()
            Restaurante.remover_restaurante()
            he.voltar_menu()
        elif opcao_escolhida == 5:
            he.exibir_subtitulo('ENVIE SEU FEEDBACK')
            listar_restaurante()
            Restaurante.receber_avaliacao()
            he.voltar_menu()
        elif opcao_escolhida == 6:
            finalizar_app()
        else:
            he.opcao_invalida()
    except (ValueError, TypeError):
        he.opcao_invalida()
            

    
def finalizar_app():
   he.exibir_subtitulo('Finalizando App')
   sys.exit()
   

def listar_restaurante():
    if not Restaurante.restaurantes:
        print('Nenhum Restaurante cadastrado ainda')
        return
    print(f"{'Nome do Restaurante'.ljust(25)} | {'Categoria'.ljust(25)} | {'Avaliação'.ljust(25)} | {'Status'.ljust(25)} | {'Cadastro'.ljust(25)}")
    for restaurante in Restaurante.restaurantes:
        print(f"{restaurante._nome.ljust(25)} | "
              f"{restaurante._categoria.ljust(25)} | "
              f"{str(restaurante.media_notas).ljust(25)} | "
              f"{restaurante.ativo.ljust(24)} | "
              f"{str(restaurante._codigo_unico).ljust(25)}")

def main():
    while True:
        os.system('cls')
        he.exibir_nome_do_programa()
        exibir_opcoes()
        escolher_opcoes()

if __name__ == '__main__':
    main()  
