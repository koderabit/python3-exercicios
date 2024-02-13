#Crie um programa que declare uma matriz de dimensão 3×3 e preencha com valores lidos pelo teclado. No final, mostre a matriz na tela, com a formatação correta.
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for linha in range(0, 3):
    for coluna in range(0, 3):
        matriz[linha][coluna] = int(input(f'Digite o valor desejado para a matriz [{linha}][{coluna}]: '))
        if coluna == 2:
            print()
print('==' * 30)
print('Matriz de tamanho 3x3 formatada:')
for linha in range(0, 3):
    for coluna in range(0, 3):
        print(f'[{(matriz[linha][coluna]):0>5}]', end=' ')
        if coluna < 2:
            print('x', end=' ' )
    print()
print('==' * 30)
