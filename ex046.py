#faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artifício indo de 10 a 0, com uma pausa de 1 segundo entre eles.
from time import sleep
print('Vai começar a contagem regressiva para a queima de fogos de artifício!!!!')

for contagem in range(10, -1, -1):
    print(contagem)
    sleep(1)
print('\U0001F386 \U0001F386 \U0001F386 \U0001F386 \U0001F386 \U0001F386')