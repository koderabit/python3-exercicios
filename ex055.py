#faça um programa que leia o peso de 5 pessoas e no final mostre qual foi o maior e o menor peso lido.
maior = 0.0
menor = 0.0

for peso in range(1, 6):
    p = float(input(f'Digite o peso da {peso}ª pessoa em Kg: '))
    if peso == 1:
        maior = p
        menor = p
    else:
        if p > maior:
            maior = p
        if p < menor:
            menor = p
print(f'O maior peso da sequência foi de {maior:.1f}Kg e o menor foi de {menor:.1f}Kg.')
