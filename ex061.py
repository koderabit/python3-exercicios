#Refaça o desafio 051, lendo o primeiro termo e razão de uma PA, mostrando os 10 primeiros termos da progressão utilizando o while.
termo = int(input('Digite o valor do primeiro termo da progressão aritimética: '))
razao = int(input('Digite o valor da razão da PA: '))
qtd = 1
while qtd <= 10:
    print(f'{qtd}° termo: {termo}')
    termo += razao
    qtd +=1
 