from modelos.restaurante_final import Restaurante
from modelos.cardapio.bebida import Bebida
from modelos.cardapio.prato import Prato

# Adicionando restaurante e bebidas
restaurante_praca = Restaurante('Praça','Gourmet')
bebida_refri = Bebida('Coca-Cola', 8, 'grande')
prato_churras = Prato('Picanha', 20, 'Churrasquiiin')

# Adicionando no cardápio
restaurante_praca.adicionar_no_cardapio(bebida_refri)
restaurante_praca.adicionar_no_cardapio(prato_churras)
def main():

    restaurante_praca.exibir_cardapio
     
if __name__ == '__main__':
    main()
