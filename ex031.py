#Desenolva um programa que pergunte a distância de uma viagem em km.
#Faça o programa calcular o valor da passagem, cobrando R$ 0,50 por km para viagens até 200km.
#e R$ 0,45 por km para viagens acima de 200km.
print('#' * 21)
print('# KoderaBit Turismo #')
print('#' * 21)
distancia = float(input('Qual a distância da sua viagem em Km? '))
if(distancia > 200):
    print('O preço da sua passagem é de R$ {:.2f}.'.format(distancia * 0.45))
else:
    print('O preço da sua passagem é de R$ {:.2f}.'.format(distancia * 0.50))
print('Agradecemos por nos escolher, esperamos que você tenha uma viagem segura e confortável.')
