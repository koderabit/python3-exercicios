# Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência. No final, mostre uma listagem de preços, organizando os dados em forma tabular.
produtos_informatica = (
    'Notebook', 2200,
    'Desktop', 1800,
    'Monitor', 500,
    'Teclado', 80,
    'Mouse', 50,
    'Impressora', 300,
    'Roteador', 120,
    'Webcam', 70,
    'Caixas de Som', 100,
    'Pen Drive', 30
)
cont = 20
print('=='*25)
print('{:-^50}'.format('TABELA DE PRODUTOS'))
print('=='*25)
for itens in range(0, len(produtos_informatica), 2):
    produto = produtos_informatica[itens]
    preco = produtos_informatica[itens+1]
    linha_formatada = '{:.<35} R${:>12,.2f}'.format(produto, preco)
    print(linha_formatada[:50])
print('=='*25)
