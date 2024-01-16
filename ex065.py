#Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre eles e qual foi o menor e o maior valor lido. O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.
qtd = soma = maior =  menor = 0
while True:
    n = int(input(f'Digite o {qtd+1}º valor: '))
    qtd+=1
    soma += n
    if qtd == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        elif n < menor:
            menor = n
    opcao = input('Você deseja acrescentar mais algum valor? [S/N]\nOpção: ').lower().strip()
    if opcao == 's':
        continue
    else:
        break
media = soma / qtd
print(f'A média total entre os números lidos foi de {media}, o maior número entre eles foi o número {maior} e o menor foi o número {menor}.')
