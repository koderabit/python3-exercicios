# Faça um algoritimo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.
price = float(input('Digite o preço original do produto: R$ '))
print('Na liquidação, o valor do produto, com 5% de desconto será de R${:.2f}.'.format(price*0.95))
