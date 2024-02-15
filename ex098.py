#Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: início, fim e passo. Seu programa tem que realizar três contagens através da função criada:
# a) de 1 até 10, de 1 em 1
# b) de 10 até 0, de 2 em 2
# c) uma contagem personalizada
from time import sleep
def contador():
    print('==' * 25)
    print('Contagem de 1 até 10 de 1 em 1:')
    for i in range(1, 11):
        print(i, flush=True, end=' ')
        sleep(0.3)
    print('FIM!')

    print('==' * 25)
    print('Contagem de 10 até 1 de 1 em 1:')
    for i in range(10, 0, -1):
        print(i, flush=True, end=' ')
        sleep(0.3)
    print('FIM!')

    print('==' * 25)
    print('Agora é a sua vez de personalizar a contagem.')
    print('--' * 25)
    inicio = int(input('INÍCIO: '))
    print('--' * 25)
    fim = int(input('FIM: '))
    print('--' * 25)
    passo = int(input('PASSO: '))
    print('--' * 25)
    if passo == 0:
        passo = 1
    if passo < 0:
        passo = passo * (-1)
    print(f'Contagem personalizada de {inicio} até {fim} de {passo} em {passo}')
    if inicio < fim:
        for i in range(inicio, fim + passo, passo):
            print(i, flush=True, end=' ')
            sleep(0.3)
        print('FIM!')
    
    elif inicio > fim:
        for i in range(inicio, fim - passo, -passo):
            print(i, flush=True, end=' ')
            sleep(0.3)
        print('FIM!')
    
    
contador()
