#crie um programa que mostre na tela todos os números pares que estão dentro do intervalo de 1 e 50
from time import sleep
print('Números pares entre 1 e 50: \n')
for pares in range(2, 51, 2):
    print(pares, end=' ')
    sleep(0.015)
print('FIM')