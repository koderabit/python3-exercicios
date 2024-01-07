#desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final mostre os 10 primeiros termos desta PA.
termo = int(input('Digite o valor do primeiro termo da progressão aritimética: '))
razao = int(input('Digite o valor da razão da PA: '))

for pa in range(1, 11):
    print(f'{pa}° termo: {termo}')
    termo += razao
