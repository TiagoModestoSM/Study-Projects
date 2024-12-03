nome_usuario = ' '
senha_usuario = ' '

def informacao():
    global nome_usuario, senha_usuario
    print('Bem Vindo! Digite suas informções de login abaixo: ')
    opcao = int(input('Deseja se Cadastrar(1) ou fazer Login(2)?\n'))
    if opcao == 1:
        nome_usuario, senha_usuario = cadastro()
        informacao(nome_usuario, senha_usuario)
    elif opcao == 2:
        if nome_usuario == ' ' and senha_usuario == ' ':
            print('Faça seu cadastro primeiro')
            informacao()
        else:
            login()
    else:
        print('Digite um número válido')

def cadastro():
    nome_usuario = input('Cadastre um nome para seu usuário: ')
    senha_usuario = input('Cadastre uma senha para seu usuário: ')
    informacao()
    return nome_usuario, senha_usuario

def login(nome_usuario,senha_usuario):
    tentativas = 0
    while True: 
        nome = input('Digite o nome de usuário: ')
        senha = input('Digite sua senha: ')
        tentativas += 1

        if nome == nome_usuario and senha == senha_usuario:
            #print('Login bem sucedido')
            print(f'Login bem-sucedido! Total de tentativas: {tentativas}')
            break
        else:
            print(f'Seu nome de usuário ou senha estão incorretos,tente novamente!\n Tentativas feitas: {tentativas}')

def main():
    informacao()

if __name__ == '__main__':
    main()