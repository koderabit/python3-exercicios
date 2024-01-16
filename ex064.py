#Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o número 999, que é a condição de parada. No final mostre quantos números foram digitados e qual a soma entre eles. (Desconsiderando o flag).
qtd = 0
soma = 0
print('Escolha um número inteiro qualquer, caso decida parar, digite 999 e pressione enter.')
while True:
    n = int(input(f'Digite o {qtd+1}º valor: '))
    if n == 999:
        break
    else:
        qtd+=1
        soma += n
print(f'Foram lidos {qtd} valores e a soma entre eles vale {soma}.')
