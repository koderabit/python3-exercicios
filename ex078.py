#Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.
lista = []
maior = menor = 0
for n in range(0, 5):
    lista.append(int(input(f'Digite um número inteiro para a posição {n}: ')))
    if n == 0:
        maior = menor = lista[0]
    else:
        if lista[n] > maior:
            maior = lista[n]
        if lista[n] < menor:
            menor = lista[n]
print(f'Os números digitados foram: {lista}.')
print(f'O menor número foi o {menor} encontrado nas posições: ', end='')
for pos, num in enumerate(lista):
    if num == menor:
        print(f'{pos}... ', end='')
print()

print(f'O maior número foi o {maior} encontrado nas posições... ', end='')
for pos, num in enumerate(lista):
    if num == maior:
        print(f'{pos}... ', end='')
print()
