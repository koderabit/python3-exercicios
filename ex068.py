# Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.
from random import randint
print('=-='*8)
print('JOGO DO PAR OU ÍMPAR')
print('=-='*8)
win = 0
while True:
    computador = randint(0,100)
    usuario = input('\nVocê escolher par ou ímpar? [P/I]: ').strip()[0]
    if usuario in 'pPiI':
        valorUser = int(input('Qual valor você escolhe?: '))
        print('=-='*25)
    else:
        continue
    
    if (valorUser + computador) % 2 == 0:
        resultado = 'PAR'
    else:
        resultado = 'ÍMPAR'

    if (usuario in 'pP' and resultado == 'PAR' or (usuario in 'iI' and resultado == 'ÍMPAR')):
        win += 1
        print(f'você escolheu {valorUser} e eu escolhi {computador}, então o resultado foi {resultado} e você venceu!')
    else:
        print(f'você escolheu {valorUser} e eu escolhi {computador}, então o resultado foi {resultado} e você perdeu!')
        break
    print('Vamos jogar novamente...')
print(f'GAME OVER... Total de vitórias consecutivas: {win}.')
