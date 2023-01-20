# Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado e a qtd de dias pelos quais
# ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$ 60 por dia e R$ 0,15 por km rodado
dia = float(input('Por quantos dias o carro ficou alugado? '))
km = float(input('Quantos quilômetros foram percorridos durante este período? Km '))
print('O preço total a pagar pela locação do veículo é de R${:.2f}.'.format((60 * dia) + (0.15 * km)))
