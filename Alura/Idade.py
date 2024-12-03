
def nome_do_programa():
    print('Diga sua idade')

def estado():
    idade = int(input('Digite sua Idade: '))
    if idade >= 18:
        print('Você é Adulto')
    elif 13<=idade<18:
        print('Você é Adolescente')
    elif idade<=0:
        print('Não é possível ter idade negativa')
        estado()
    else:
        print('Você é Criança')


def main(): 
    nome_do_programa()
    estado()

    
if __name__ == '__main__':
    main()