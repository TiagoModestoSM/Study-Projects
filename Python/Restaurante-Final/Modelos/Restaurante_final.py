from modelos.avaliacao import Avaliacao
from modelos.cardapio.item_cardapio import ItemCardapio
from assests import data_hora
import random

class Restaurante:
    restaurantes = []
    numeros_cadastrados = []

    def __init__(self, nome, categoria):
        self._nome = nome.title()
        self._categoria = categoria.upper()
        self._ativo = False
        self._avaliacao = []
        self._cardapio = []
        self._codigo_unico = None
        Restaurante.restaurantes.append(self)

    def __str__(self):
        return f'{self._nome} | {self._categoria}'


    @classmethod
    def cadastrar_novo_restaurante(cls):
        nome = input("Digite o nome do restaurante: ").strip()
        categoria = input("Digite a categoria: ").strip()

        if nome and categoria:
            novo_restaurante = cls(nome, categoria)
            novo_restaurante._codigo_unico = cls.codigo_unico()
            print(f'Restaurante "{novo_restaurante._nome}" cadastrado com sucesso em {data_hora.data_formatada} às {data_hora.hora_formatada} ')
        else:
            print("Nome ou categoria inválidos.")

    @classmethod
    def codigo_unico(cls):
        while True:
            codigo = random.randint(1000000000, 9999999999)
            if codigo not in cls.numeros_cadastrados:
                cls.numeros_cadastrados.append(codigo)
                return codigo

    @classmethod
    def alternar_estado(cls):
        codigo = input("Digite o código do restaurante que deseja ativar/desativar: ")
        restaurante_encontrado = False
        for restaurante in cls.restaurantes:
            if str(restaurante._codigo_unico) == codigo:
                restaurante._ativo = not restaurante._ativo
                print(f"O restaurante '{restaurante._nome}' teve seu estado alterado para {'Ativo' if restaurante._ativo else 'Inativo'}")
                restaurante_encontrado = True
                break
        if not restaurante_encontrado:
            print("Restaurante não encontrado.")

    @property
    def ativo(self):
        return '✅' if self._ativo else '❌'

    def receber_avaliacao(self, cliente, nota):
        if isinstance(nota, int) and 0 < nota <= 5:
            avaliacao = Avaliacao(cliente, nota)
            self._avaliacao.append(avaliacao)

    @property
    def media_notas(self):
        if not self._avaliacao:
            return '-'
        soma_das_notas = sum(avaliacao._nota for avaliacao in self._avaliacao)
        quantidade_de_notas = len(self._avaliacao)
        media = round(soma_das_notas / quantidade_de_notas, 1)
        return media

    def adicionar_no_cardapio(self, item):
        if isinstance(item, ItemCardapio):
            self._cardapio.append(item)

    @property
    def exibir_cardapio(self):
        print(f'Cardápio do restaurante: {self._nome}')
        for i, item in enumerate(self._cardapio, 1):
            if hasattr(item, 'descricao'):
                mensagem_prato = f'{i}. Nome:{item._nome} | Preço: R${item._preco} | Descrição: {item.descricao}'
                print(mensagem_prato)
            else:
                mensagem_bebida = f'{i}. Nome:{item._nome} | Preço: R${item._preco} | Tamanho: {item.tamanho}'
                print(mensagem_bebida)
