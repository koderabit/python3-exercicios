#Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno retangular (largura e comprimento) e mostre a área do terreno.
def area():
    print(f'{'Controle de terreno':^50}')
    print('--'*25)
    x = float(input('LARGURA (m): '))
    y = float(input('COMPRIMENTO (m): '))
    a = x * y
    print(f'A área de um terreno {x:.1f}m x {y:.1f}m é de {a:.1f}m².')


area()
