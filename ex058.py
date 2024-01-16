# Melhore o jogo do desafio 028 onde o computador vai "pensar" em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar. Mostre no final quantas tentativas foram necessárias.
from time import sleep
from random import randint
numComput = randint(1, 10)

print('Eu pensei em um número entre 1 e 10, você consegue adivinhar?\n')
tentativas = 0
msgWin = (f'Você acertou! Número de tentativas: ')
msgLose1 = ('Você errou, tente novamente um número maior: ')
msgLose2 = ('Você errou, tente novamente um número menor: ')
while True:
    numUsuario = int(input('\nTente adivinhar o número que eu pensei: '))
    tentativas += 1
    if numComput == numUsuario:
        for letra in msgWin:
            print(letra, end='', flush=True)
            sleep(0.01)
        break
    else:
        if numComput > numUsuario:
            for letra in msgLose1:
                print(letra, end='', flush=True)
                sleep(0.01)
        else: 
            for letra in msgLose2:
                print(letra, end='', flush=True)
                sleep(0.01)
print(f'{tentativas}.')