# Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem crescente.
lista = []
while True:
    num = int(input('Qual número você deseja adicionar à lista? '))
    if num in lista:
        print('Número já existente na lista...')
    else:
        print('Número adicionado com sucesso...')
        lista.append(num)
    print('=='*25)
    continuar = input('Você deseja continuar? [S/N]: ').strip()
    while continuar not in 'sSnN':
        continuar = input('Você deseja continuar? [S/N]: ').strip()
    if continuar in 'sS':
        continue
    else:
        break
lista.sort()
print('=='*25)
print(f'valores digitados: {lista}.')
