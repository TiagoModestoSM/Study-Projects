# Cria a função de voltar menu
def voltar_menu():
    input('\nDigite uma tecla para voltar ao menu principal: ')
    from app import main
    main()

# Cria a função de opção invalida
def opcao_invalida():
    print('Opção Inválida')
    voltar_menu()

# Cria a função que verifica a hora e a data
def date_time():
    import datetime
    from datetime import datetime
    agora = datetime.now()
    data_formatada = agora.strftime('%d/%m/%Y')
    hora_formatada = agora.strftime('%H:%M:%S')
    return data_formatada, hora_formatada

# Cria a função que exibibe o nome do programa
def exibir_nome_do_programa():
    '''Essa função exibe o nome do programa na tela de comando'''
    print("""
█████████████████████▀███████████████████████████████████████████████████████████████
█─▄─▄─█▄─▄██▀▄─██─▄▄▄▄█▄─██─▄█▄─▄█▄─▀█▄─▄███─▄▄▄─█─▄▄─█▄─▀█▀─▄█▄─▄█▄─▄▄▀██▀▄─██─▄▄▄▄█
███─████─███─▀─██─██▄─██─██─███─███─█▄▀─████─███▀█─██─██─█▄█─███─███─██─██─▀─██▄▄▄▄─█
▀▀▄▄▄▀▀▄▄▄▀▄▄▀▄▄▀▄▄▄▄▄▀▀▄▄▄▄▀▀▄▄▄▀▄▄▄▀▀▄▄▀▀▀▄▄▄▄▄▀▄▄▄▄▀▄▄▄▀▄▄▄▀▄▄▄▀▄▄▄▄▀▀▄▄▀▄▄▀▄▄▄▄▄▀
""")

# Cria a função que exibe o subtítulo do programa

def exibir_subtitulo(texto):
    import os
    os.system('cls')
    linha = '=' * (len(texto))
    print(linha)
    print(texto)
    print(linha)
    print()
