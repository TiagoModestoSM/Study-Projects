nome_usuario = ''  # Variáveis globais para armazenar os dados do usuário
senha_usuario = ''

def informacao():
    global nome_usuario, senha_usuario  # Referência às variáveis globais
    print('Bem-vindo! Digite suas informações de login abaixo:')
    opcao = int(input('Deseja se Cadastrar (1) ou fazer Login (2)?\n'))
    
    if opcao == 1:
        nome_usuario, senha_usuario = cadastro()  # Captura o retorno de cadastro
        login(nome_usuario, senha_usuario)  # Realiza o login após o cadastro
    elif opcao == 2:
        if nome_usuario == '' and senha_usuario == '':  # Verifica se o cadastro foi feito
            print('Faça seu cadastro primeiro.')
            informacao()  # Chama novamente para o usuário se cadastrar
        else:
            login(nome_usuario, senha_usuario)  # Realiza o login com as credenciais cadastradas
    else:
        print('Digite um número válido.')

def cadastro():
    nome_usuario = input('Cadastre um nome para seu usuário: ')
    senha_usuario = input('Cadastre uma senha para seu usuário: ')
    return nome_usuario, senha_usuario  # Retorna as credenciais para a função informacao

def login(nome_usuario, senha_usuario):
    tentativas = 0
    while True:
        nome = input('Digite o nome de usuário: ')
        senha = input('Digite sua senha: ')
        tentativas += 1

        if nome == nome_usuario and senha == senha_usuario:
            print(f'Login bem-sucedido! Total de tentativas: {tentativas}')
            break
        else:
            print(f'Seu nome de usuário ou senha estão incorretos. Tente novamente!\nTentativas feitas: {tentativas}')

def main():
    informacao()  # Inicia o processo de cadastro ou login

if __name__ == '__main__':
    main()  # Inicia o programa
