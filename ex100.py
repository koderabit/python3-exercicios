#Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar(). A primeira função vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai mostrar a soma entre todos os valores pares sorteados pela função anterior.
from random import randint
numeros = []
def sorteia():
    print('==' * 40)
    print('Sorteando 5 números para uma lista: ', end=' ')
    for i in range(0, 5):
        numeros.append(randint(-1000, 1000))
        if i < 3:
            print(numeros[i], end=', ')
        elif i == 3:
            print(numeros[i], end=' e ')
        else:
            print(f'{numeros[i]}.')
    print('--'*40)

def somaPar(lista):
    soma = par = 0
    for num in lista:
        if num % 2 == 0:
            soma += num
            par += 1
    print(f'Ao todo foram encontrados {par} números pares e a soma entre eles vale {soma}.')
    print('==' * 40)
sorteia()
somaPar(numeros)
