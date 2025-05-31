# Crie um programa que faça o computador jogar Jokenpô com você.
from time import sleep
from random import randint

computador = randint(1, 3)
'''frase = "Olá..."
for letra in frase:
    print(letra, end='', flush=True)
    sleep(0.2)'''

msg = '''Olá, você gostaria de jogar JOKENPÔ comigo?
Este é o famoso jogo do pedra, papel, tesoura. Vou explicar as regras:
PEDRA ganha da TESOURA mas perde para o PAPEL.
TESOURA ganha do PAPEL mas perde para a PEDRA.
PAPAEL ganha da PEDRA mas perde para a TESOURA.
-----------------------------------------------------------------------
'''
for letra in msg:
    print(letra, end='', flush=True)
    sleep(0.01)

msg2 = '''Agora que você conhece as regras, escolha a sua opção:
[1] DIGITE 1 PARA ESCOLHER PEDRA
[2] DIGITE 2 PARA ESCOLHER PAPEL
[3] DIGITE 3 PARA ESCOLHER TESOURA
-----------------------------------------------------------------
'''
for letra in msg2:
    print(letra, end='', flush=True)
    sleep(0.01)

usuario = int(input('Opção: '))

msg3 = 'PEDRA \U0001F44A, PAPEL \U0001F590, TESOURA \U0000270C ...\n\n'
for letra in msg3:
    print(letra, end='', flush=True)
    sleep(0.1)

if usuario == 1:
    if computador == 1:
        print('VOCÊ ESCOLHEU PEDRA E EU TAMBÉM, JOGO EMPATADO!!')
    elif computador == 2:
        print('VOCÊ ESCOLHEU PEDRA E EU ESCOLHI PAPEL, HAHAHAHAHA, EU GANHEI!!')
    elif computador == 3:
        print('VOCÊ ESCOLHEU PEDRA E EU ESCOLHI TESOURA, VOCÊ GANHOU!! SORTE DE PRINCIPIANTE...')

elif usuario == 2:
    if computador == 1:
        print('VOCÊ ESCOLHEU PAPEL E ESCOLHI PEDRA, VOCÊ GANHOU!! SORTE DE PRINCIPIANTE...')
    elif computador == 2:
        print('VOCÊ ESCOLHEU PAPEL E EU TAMBÉM, JOGO EMPATADO!!')
    elif computador == 3:
        print('VOCÊ ESCOLHEU PAPEL E EU ESCOLHI TESOURA, HAHAHAHAHA, EU GANHEI!!')

elif usuario == 3:
    if computador == 1:
        print('VOCÊ ESCOLHEU TESOURA E EU ESCOLHI PEDRA, HAHAHAHAHA, EU GANHEI!!')
    elif computador == 2:
        print('VOCÊ ESCOLHEU TESOURA E EU ESCOLHI PAPEL, VOCÊ GANHOU!! SORTE DE PRINCIPIANTE...')
    elif computador == 3:
        print('VOCÊ ESCOLHEU TESOURA E EU TAMBÉM, JOGO EMPATADO!!')
else:
    print('Opção inválida, jogue novamente.')

msg4 = 'Obrigado por jogar comigo, me diverti muito, até a próxima...'
for letra in msg4:
    print(letra, end='', flush=True)
    sleep(0.015)


