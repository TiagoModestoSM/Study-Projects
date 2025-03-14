from modelos.restaurante_final import Restaurante

restaurante_praca = Restaurante('Praça','Gourmet')
restaurante_praca.receber_avaliacao('Tiago',10)
restaurante_praca.receber_avaliacao('Ester', 8)
restaurante_praca.receber_avaliacao('Sara', 6)


def main():
    Restaurante.listar_restaurantes()
    
if __name__ == '__main__':
    main()