# Crie um programa que leia quanto dinheiro uma pessoa tem e mostre quantos dólares ela pode comprar.
# Considerar o valor do dólar: US$ 1,00 = R$ 3,27
dol = float(3.27)
din = float(input('Quantos reais você tem na carteira agora? R$ '))
print('Com R${:.2f}, você poderia comprar US${:.2f} hoje, considerando que o dólar está custando R$3,27.'.format(din, din/dol))


