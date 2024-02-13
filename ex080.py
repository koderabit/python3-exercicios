# Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, já na posição correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.
lista = []
for n in range(0, 5):
    num = int(input(f'Digite o {n+1}º valor inteiro... '))
    pos = 0
    while pos < len(lista) and num > lista[pos]:
        pos += 1
    lista.insert(pos, num)
    print(f'Valor adicionado na posição {pos}.')
print('=='*50)
print(f'Valores digitados, em ordem crescente, sem usar o método sort: {lista}.')
