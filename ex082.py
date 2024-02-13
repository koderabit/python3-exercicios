# Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente. Ao final, mostre o conteúdo das três listas geradas.
lista = []
par = []
impar = []
c = 0
while True:
    lista.append(int(input(f'Digite o {c+1}º valor inteiro... ')))
    c += 1
    resp = input('Você deseja adicionar outro número? [S/N]: ').strip()
    while resp not in 'sSnN':
        resp = input('Você deseja adicionar outro número? [S/N]: ').strip()
    if resp in 'sS':
        continue
    else:
        break
lista.sort()
for num in lista:
    if num % 2 == 0:
        par.append(num)
    else:
        impar.append(num)
print('=='*30)
print(f'Lista completa dos números digitados: {lista}.')
print(f'Lista com somente os números pares: {par}.')
print(f'Lista com somente os números ímpares: {impar}.')
