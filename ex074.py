# Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.
from random import randint
numeros = (randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100))
maior = menor = 0
print('Números escolhidos aleatoriamente: ', end='')
for c, numero in enumerate(numeros):
    print(numero, end=' ')
    if c == 0:
        maior = numero
        menor = numero
    else:
        if numero > maior:
            maior = numero
        if numero < menor:
            menor = numero
print(f'\nO menor número foi {menor} e o maior número foi {maior}.')