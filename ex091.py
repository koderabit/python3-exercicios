#Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses resultados em um dicionário em Python. No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.
from random import randint
from time import sleep
from operator import itemgetter
jogadores = dict()
for i in range(1, 5):
    jogadores[f'jogador{i}'] = randint(1, 6)
print()
print(f'{'VALORES SORTEADOS':-^50}')
print()
for k, v in jogadores.items():
    sleep(0.5)
    print(f'O {k} tirou o número {v} no dado.')
print()
print(f'{'RANKING DE JOGADORES':-^50}')
print()
ranking = dict()
ranking = sorted(jogadores.items(), key=itemgetter(1), reverse=True)

for n, rank in enumerate(ranking):
    sleep(0.5)
    print(f'{n+1}º lugar: {rank[0]} que tirou o número {rank[1]}.')
print('-'*50)