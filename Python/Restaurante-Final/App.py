from modelos.restaurante_final import Restaurante
from modelos.cardapio.bebida import Bebida
from modelos.cardapio.prato import Prato
restaurante_praca = Restaurante('Praça','Gourmet')
bebida_refri = Bebida('Coca-Cola', 8, 'grande')
prato_churras = Prato('Picanha', 20, 'FAZ O L')
def main():
    print(bebida_refri)
    print(prato_churras)
    
if __name__ == '__main__':
    main()