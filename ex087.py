#Aprimore o desafio anterior, mostrando no final:
# A) A soma de todos os valores pares digitados.
# B) A soma dos valores da terceira coluna.
# C) O maior valor da segunda linha.
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

for linha in range(0, 3):
    for coluna in range(0, 3):
        matriz[linha][coluna] = int(input(f'Digite o valor desejado para a matriz: [{linha+1}ª linha] x [{coluna+1}ª coluna]: '))
        if coluna == 2:
            print()
print('==' * 30)
somaPar = somaTerceiraColuna = 0
maiorValor = matriz[1][0]
print('Matriz de tamanho 3x3 formatada:')
for linha in range(0, 3):
    for coluna in range(0, 3):
        if matriz[linha][coluna] % 2 == 0:
            somaPar += matriz[linha][coluna]
        if coluna == 2:
            somaTerceiraColuna += matriz[linha][coluna]
        if linha == 1:
            if matriz[linha][coluna] > maiorValor:
                maiorValor = matriz[linha][coluna]
        print(f'[{(matriz[linha][coluna]):0>5}]', end=' ')
        if coluna < 2:
            print('x', end=' ' )
    print()
print('==' * 30)
print(f'''A soma de todos os valores pares digitados é igual a {somaPar}.
A soma dos valores da terceira coluna vale {somaTerceiraColuna}.
E o maior valor da segunda linha foi o número {maiorValor}.''')
