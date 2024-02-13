estatistica = dict()
estatistica['nome'] = input('Nome do Jogador: ').upper().strip()
total_partidas = int(input(f'Quantas partidas o {estatistica["nome"]} jogou na temporada? '))
gols_marcados = []
for i in range(0, total_partidas): 
    gols_marcados.append(int(input(f'Quantos gols o {estatistica["nome"]} fez na {i+1}ª partida? ')))
estatistica['gols'] = gols_marcados[:]
estatistica['total de gols'] = sum(gols_marcados[:])
print(f'{'KODERABIT STATS':-^100}')
print('=='*50)
print(estatistica)
print('=='*50)
for k, v in estatistica.items():
    print(f'{k.upper():-<50}{v!s:->50}')
print('=='*50)
print(f'O jogador {estatistica["nome"]} tem {total_partidas} partidas na temporada: ')
for i, gol in enumerate(gols_marcados):
    print(f'Na {i+1}ª partida ele marcou {gol} gols.')
print(f'No total foram {estatistica["total de gols"]} gols em {total_partidas} jogos e a sua média de gol foi de {estatistica["total de gols"] / total_partidas:.2f} gols por jogo.')
print('=='*50)
