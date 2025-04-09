import os, datetime, random
from datetime import datetime
from modelos.restaurante_final import Restaurante
from modelos.cardapio.bebida import Bebida
from modelos.cardapio.prato import Prato
import utils.helpers as he


def exibir_opcoes():
    print('1. Cadastrar Restaurante')
    print('2. Listar Restaurante')
    print('3. Alterar Estado do Restaurante')
    print('4. Remover Restaurante')
    print('5. Sair')

def escolher_opcoes():
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))
        
        if opcao_escolhida == 1:
            os.system('cls')
            he.exibir_subtitulo('CADASTRO DE NOVOS RESTAURANTES')
            Restaurante.cadastrar_novo_restaurante()
            he.voltar_menu()
        elif opcao_escolhida == 2:
            os.system('cls')
            he.exibir_subtitulo('LISTA DE RESTAURANTES')
            listar_restaurante()
            he.voltar_menu()
        elif opcao_escolhida == 3:
            os.system('cls')
            listar_restaurante()
            Restaurante.alternar_estado()
            he.voltar_menu()
        elif opcao_escolhida == 5:
            finalizar_app()
        else:
            he.opcao_invalida()
    except:
        he.opcao_invalida()
            

    
def finalizar_app():
   he.exibir_subtitulo('Finalizando App')
   exit
   

def listar_restaurante():
    print(f"{'Nome do Restaurante'.ljust(25)} | {'Categoria'.ljust(25)} | {'Avaliação'.ljust(25)} | {'Status'.ljust(25)} | {'Cadastro'.ljust(25)}")
    for restaurante in Restaurante.restaurantes:
        print(f"{restaurante._nome.ljust(25)} | "
              f"{restaurante._categoria.ljust(25)} | "
              f"{str(restaurante.media_notas).ljust(25)} | "
              f"{str(restaurante.ativo).ljust(24)} | "
              f"{str(restaurante._codigo_unico).ljust(25)}")

def main():
    os.system('cls')
    he.exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcoes()

if __name__ == '__main__':
    main()  
