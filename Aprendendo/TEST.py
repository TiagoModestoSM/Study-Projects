import random

cadastro_unico = random.randint(0, 9999999999)

restaurantes = [{'nome': 'Pizzas', 'categoria': 'Pizza', 'ativo': True, 'cadastro': '0000000'}]

nome_restaurante = input('Digite o Nome do Restaurante que deseja cadastrar: \n')
categoria = input(f'Digite a categoria do restaurante {nome_restaurante}: ')

dados_do_restaurante = {'nome': nome_restaurante, 'categoria': categoria, 'ativo': False, 'cadastro': cadastro_unico}
restaurantes.append(dados_do_restaurante)

print(f"{'|NOME DO RESTAURANTE'.ljust(24)} | {'CATEGORIA'.ljust(20)} | {'STATUS'.ljust(20)}| {'CADASTRO'.ljust(20)}|")
for i, restaurante in enumerate(restaurantes, start=1):
    nome_restaurante = restaurante['nome']
    categoria_restaurante = restaurante['categoria']
    ativos_restaurante = 'Ativado' if restaurante['ativo'] else 'Desativado'
    restaurante_cadastrado = restaurante['cadastro']
    print(f"|{i}. {nome_restaurante.ljust(20)} | {categoria_restaurante.ljust(20)} | {ativos_restaurante.ljust(20)}| {str(restaurante_cadastrado).ljust(20)}|")
def remover_restaurante():
    restaurante_removido = input('Digite o código do restaurante que deseja remover: ')
    encontrado = False  # Para verificar se o restaurante foi encontrado

    for i, restaurante in enumerate(restaurantes):
        if restaurante_removido == str(restaurante['cadastro']):  # Comparar como string
            del restaurantes[i]  # Remove o restaurante da lista
            print(f'O restaurante com código {restaurante_removido} foi removido com sucesso.')
            encontrado = True
            break  # Encerra o loop após remover

    if not encontrado:
        print('Restaurante não encontrado.')
