# Crie um programa que vai ler vários números e colocar em uma lista. Depois disso mostre: 
# A) Quantos números foram digitados.
# B) A lista de valores, ordenada de forma decrescente.
# C) Se o valor 5 foi digitado e está ou não na lista.
lista = []
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
lista.sort(reverse=True)
print('=='*35)
print(f'O número de elementos da lista é: {len(lista)}.')
print(f'Valores digitados em ordem decrescente: {lista}.')
if 5 in lista:
    print('O número 5 está presente na lista.')
else:
    print('O número 5 não está presente na lista.')
