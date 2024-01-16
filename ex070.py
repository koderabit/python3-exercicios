# Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:
# A) qual é o total gasto na compra.
# B) quantos produtos custam mais de R$1000.
# C) qual é o nome do produto mais barato.
print('##'*15)
print('{:^30}'.format('KODERABIT SHOPPING'))
print('##'*15)
total = acima1000 = maisBarato = qtd = 0
produtoMaisBarato = ' '
while True:
    produto = input('Digite o nome do produto: ').strip().capitalize()
    preco = float(input(f'Qual o valor do {produto}? R$ '))
    print(f'{produto} adicionado ao carrinho.')
    total += preco
    qtd += 1
    if preco > 1000.00:
        acima1000 += 1
    if qtd == 1 or preco < maisBarato:
        maisBarato = preco
        produtoMaisBarato = produto    
    opcao = ' '
    while opcao not in 'sSnN':
        opcao = input('Você deseja cadastrar mais um produto? [S/N]: ').strip()[0]
    if opcao in 'nN':
        break
print('{:-^40}'.format('PROGRAMA FINALIZADO'))
print(f'''Valor total da compra: R$ {total:.2f}.
Total de produtos acima de R$ 1000,00: {acima1000}.
O produto mais barato foi: {produtoMaisBarato}. Valor de R$ {maisBarato:.2f}.''')
