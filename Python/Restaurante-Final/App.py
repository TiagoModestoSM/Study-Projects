from Modelos.Restaurante_final import Restaurante

restaurante_praca = Restaurante('Praça','Gourmet')
restaurante_sushi = Restaurante('MaoTseTung', 'Japonesa')
restaurante_china = Restaurante('XingLing', 'Chinesa')

def main():
    Restaurante.listar_restaurantes()

if __name__ == '__main__':
    main()