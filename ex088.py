#Faça um programa que ajude um jogador da MEGA SENA a criar palpites.O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.
from random import randint
from time import sleep
listaTemp = []
listaJogos = []
print('==' * 30)
print(f'{'KODERABIT DO MILHÃO':-^60}')
print('==' * 30)
qtdJogos = int(input('Quantos jogos da megassena você deseja gerar? '))
jogos = 1
while jogos <= qtdJogos:
    c = 0
    while True:
        num = randint(1, 60)
        if num not in listaTemp:
            listaTemp.append(num)
            c += 1
        if c == 6:
            break
    jogos += 1
    listaTemp.sort()
    listaJogos.append(listaTemp[:])
    listaTemp.clear()
print(f'{f' SORTEANDO {qtdJogos} JOGOS ':=^60}')
for pos, jogo in enumerate(listaJogos):
    jogo_formatado = ', '.join(f'{num:02d}' for num in jogo)
    print(f'{pos+1:0>2d}º jogo: [{jogo_formatado}]'.rjust(35))
    sleep(0.2)
print(f'{' BOA SORTE ':=^60}')
