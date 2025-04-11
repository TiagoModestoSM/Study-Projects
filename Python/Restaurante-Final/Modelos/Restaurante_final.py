from modelos.avaliacao import Avaliacao
from modelos.cardapio.item_cardapio import ItemCardapio
import utils.helpers as he
from InquirerPy import inquirer
import random

data, hora = he.date_time()
class Restaurante:
    restaurantes = []
    numeros_cadastrados = []
    categorias = [ "Japonesa", "Brasileira", "Italiana", "Mexicana", "Árabe"]
    def __init__(self, nome, categoria):
        self._nome = nome.title()
        self._categoria = categoria.title()
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
        categoria = cls.escolher_categoria()

        if nome and categoria:
            novo_restaurante = cls(nome, categoria)
            novo_restaurante._codigo_unico = cls.codigo_unico()
            print(f'Restaurante "{novo_restaurante._nome}" cadastrado com sucesso em {data} às {hora} ')
        else:
            print("Nome ou categoria inválidos.")
    
    @classmethod
    def remover_restaurante(cls):
        if not cls.restaurantes:
            return
        codigo = str(input('Digite o código do restaurante que deseja remover: ')).strip()
        for restaurante in cls.restaurantes:
            if str(restaurante._codigo_unico) == codigo:
                cls.restaurantes.remove(restaurante)
                print(f'Restaurante {restaurante._nome} removido com sucesso às {hora} em {data}')
                return
        print('Restaurante não encontrado')
        
    @classmethod
    def escolher_categoria(cls):
        while True:
            print('Escolha uma categoria: ')
            opcoes = cls.categorias + ['Minha categoria não está aqui']
            escolha = inquirer.select(message = 'Selecione a categoria do restaurante: ',choices = opcoes).execute()
            
            if escolha == 'Minha categoria não está aqui':
                nova_categoria = input('Digite o nome da nova categoria: ').strip().capitalize()
                if nova_categoria:
                    cls.categorias.append(nova_categoria)
                    print(f'Categoria "{nova_categoria}" cadastrada com sucesso!')
                    return nova_categoria
                else:
                    print('Categoria inválida. Tente novamente.')
            else:
                return escolha
    @classmethod
    def codigo_unico(cls):
        while True:
            codigo = random.randint(1000000000, 9999999999)
            if codigo not in cls.numeros_cadastrados:
                cls.numeros_cadastrados.append(codigo)
                return codigo

    @classmethod
    def alternar_estado(cls):
        if not cls.restaurantes:
            return
        codigo = input("Digite o código do restaurante que deseja ativar/desativar: ").strip()
        restaurante_encontrado = False
        for restaurante in cls.restaurantes:
            if str(restaurante._codigo_unico) == codigo:
                restaurante._ativo = not restaurante._ativo
                print(f"O restaurante '{restaurante._nome}' teve seu estado alterado para {'Ativo' if restaurante._ativo else 'Desativado'}")
                restaurante_encontrado = True
                break
        if not restaurante_encontrado:
            print("Restaurante não encontrado.")

    @property
    def ativo(self):
        return '✅' if self._ativo else '❌'
    


    @classmethod
    def receber_avaliacao(cls):
        if not cls.restaurantes:
            return

        codigo = input("Digite o código do restaurante que deseja avaliar: ").strip()
        for restaurante in cls.restaurantes:
            if str(restaurante._codigo_unico) == codigo:
                cliente = input("Digite seu nome: ").strip()
                try:
                    nota = int(input("Digite a nota (1 a 5): ").strip())
                    if 1 <= nota <= 5:
                        avaliacao = Avaliacao(cliente, nota)
                        restaurante._avaliacao.append(avaliacao)
                        print(f"Avaliação registrada com sucesso para o restaurante '{restaurante._nome}'!")
                    else:
                        print("Nota fora do intervalo permitido (1 a 5).")
                except ValueError:
                    print("Nota inválida. Por favor, insira um número inteiro de 1 a 5.")
                return
        print("Restaurante não encontrado.")




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
