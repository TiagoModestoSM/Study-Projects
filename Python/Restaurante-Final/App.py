from modelos.restaurante_final import Restaurante
from modelos.cardapio.bebida import Bebida
from modelos.cardapio.prato import Prato
from assests.exibir_subtitulo import exibir_subtitulo
from assests.exibir_nome_do_programa import exibir_nome_do_programa
def main():
    exibir_subtitulo('TIAGUIN COMIDAS')
    exibir_nome_do_programa()
    Restaurante.exibir_opcoes()
    Restaurante.cadastrar_novo_restaurante()

    Restaurante.listar_restaurantes()
if __name__ == '__main__':
    main()  
