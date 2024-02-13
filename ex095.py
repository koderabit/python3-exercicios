# Aprimore o desafio 93 para que ele funcione com vários jogadores, incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.
jogadores = []
estatistica = dict()
while True:
    estatistica['nome'] = input('Nome do Jogador: ').upper().strip()
    print('--'*25)
    total_partidas = int(input(f'Quantas partidas o {estatistica["nome"]} jogou na temporada? '))
    gols_marcados = []
    print('--'*25)
    for i in range(0, total_partidas): 
        gols_marcados.append(int(input(f'Quantos gols o {estatistica["nome"]} fez na {i+1}ª partida? ')))
        print('--'*25)
    estatistica['gols'] = gols_marcados[:]
    estatistica['total de gols'] = sum(gols_marcados[:])
    jogadores.append(estatistica.copy())
    print('=='*25)
    while True:
        opcao = input('Deseja cadastrar mais um jogador? [S/N]').upper().strip()[0]
        if opcao in 'SN':
            break
        print('ATENÇAÕ, DIGITE APENAS S OU N...')
        print('=='*25)
    if opcao in 'N':
        print('=='*25)
        break
    print('=='*25)
    print()
print()
print(f'{'KODERABIT STATS':-^100}')
print(f'{'COD':<3}{'JOGADOR':-^30}{'GOLS':-^62}{'TOTAL':->5}')
for num, jogador in enumerate(jogadores):
    print(f'{num+1:0>3}', end='')
    for k, v in jogador.items():
        if k == 'nome':
            print(f'{v:-^30}', end='')
        elif k == 'gols':
            print(f'{v!s:-^62}', end='')
        else:
            print(f'{v:->5}')
while True:
    cod = int(input('Digite o código do jogador para verificar o aproveitamento individual: [0 para cancelar]'))
    while cod > len(jogadores):
        cod = int(input('CÓDIGO INVÁLIDO, DIGITE NOVAMENTE: '))    
    if cod == 0:
        print('=='*50)
        break
    for i in range(0, len(jogadores)):
        if cod == i + 1:
            gols_str = ' '.join(map(str, jogadores[cod-1]['gols']))
            print()
            print('=='*50)
            print(f'{'COD':<3}{'JOGADOR':-^30}{'GOLS':-^62}{'TOTAL':->5}')  
            print(f'{cod:0>3}{jogadores[cod-1]['nome']:-^30}{gols_str!s:-^62}{jogadores[cod-1]['total de gols']:->5}')
            print()
print('=='*50)
