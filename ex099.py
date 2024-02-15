# Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros. Seu programa tem que analisar todos os valores e dizer qual deles é o maior.
from time import sleep
def maior(*num):
    m = 0
    sleep(0.4)
    print('=='*50)
    if len(num) == 0:
        print(f'Analisando os valores passados... {num}')
        print('Não foi recebido nenhum valor como parâmetro.')
        print('--'*50)
    else:
        print(f'Analisando os valores passados...', end=' ')
        for c, n in enumerate(num):
            if c < len(num) - 2: 
                print(n, end=', ') 
            elif c < len(num) - 1: 
                print(n, end=' e ') 
            else: 
                print(f'{n}.')
            if n > m:
                m = n

        print(f'\nAo todos foram informados {len(num)} números e o maior deles é o número {m}.')
        print('--'*50)


maior(5, 2, 3, 4, 6, 9)
maior(1, 5, 9, 10, 2, 97, 12, 650, 4, 66)
maior(1, 6, 41, 69, 225, 1025, 6, -5, 2558, 2)
maior(1)
maior()
