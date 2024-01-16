# Crie um programa que leia números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre elas (desconsiderando o flag).
qtd = soma = 0
while True:
    n = int(input('Digite um número inteiro... [999 para sair]: '))
    if n == 999:
        break
    soma += n
    qtd += 1

if qtd > 0:
    print(f'Você digitou {qtd} números e a soma deles vale {soma}.')
else:
    print('Você não digitou nenhum número para somar.')