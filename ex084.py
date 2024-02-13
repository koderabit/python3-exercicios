#Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
# A) Quantas pessoas foram cadastradas.
# B) Uma listagem com as pessoas mais pesadas. 
# C) Uma listagem com as pessoas mais leves.
listaTemporaria = []
listaPrincipal = []
maiorPeso = menorPeso = 0

while True:
    listaTemporaria.append(input('Qual nome você quer cadastrar? ').strip().title())
    listaTemporaria.append(float(input(f'Qual o peso de {listaTemporaria[0]}? Kg: ')))
    if len(listaPrincipal) == 0:
        maiorPeso = menorPeso = listaTemporaria[1]
    else:
        if listaTemporaria[1] > maiorPeso:
            maiorPeso = listaTemporaria[1]
        if listaTemporaria[1] < menorPeso:
            menorPeso = listaTemporaria[1]
    listaPrincipal.append(listaTemporaria[:])
    listaTemporaria.clear()
    opcao = input('\n-----> Você deseja cadastrar mais uma pessoa? S/N: ').strip().upper()
    while opcao not in 'SN':
        opcao = input('\nOpção inválida, você deseja continuar? S/N: ').strip().upper()
    if opcao == 'S':
        print()
        continue
    else:
        print()
        break
print('==' * 30)
print(f'No total foram cadastradas {len(listaPrincipal)} pessoas.')
print('==' * 30)
print('Nome e peso dos mais pesados: ', end='\n')

for maisPesado in listaPrincipal:
    if maisPesado[1] == maiorPeso:
        print(f'{maisPesado[0].title()}: {maisPesado[1]:.2f}Kg')
print('==' * 30)
print('Nome e peso dos mais leves: ', end='\n')
for maisLeve in listaPrincipal:
    if maisLeve[1] == menorPeso:
        print(f'{maisLeve[0].title()}: {maisLeve[1]:.2f}')
print('==' * 30)
