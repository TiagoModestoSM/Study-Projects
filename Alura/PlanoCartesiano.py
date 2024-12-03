#declarar os inputs para X e Y
X = int(input('Digite o valor de X: '))
Y = int(input('Digite o valor de Y: '))

if X > 0 and Y > 0:
    print('Seu ponto está no 1° quadrante')
elif X < 0 and Y > 0:
    print('Seu ponto está no 2° quadrante')
elif X < 0 and Y < 0:
    print('Seu ponto está no 3° quadrante')
elif X > 0 and Y < 0:
    print('Seu ponto está no 4° quadrante')
else:
    print('Seu ponto está na origem')