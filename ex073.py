# Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:
# a) Os 5 primeiros times.
# b) Os últimos 4 colocados.
# c) Times em ordem alfabética.
# d) Em que posição está o time da Chapecoense.
classificacao_brasileirao_2021 = (
    "Flamengo", "Palmeiras", "Atlético Mineiro", "Fortaleza", "Bragantino",
    "Corinthians", "Fluminense", "Atlético Paranaense", "Ceará", "Internacional",
    "Juventude", "Santos", "Cuiabá", "Sport", "Bahia", "São Paulo", "América-MG",
    "Grêmio", "Chapecoense", "Goiás"
)
print('=='*25)
print('{:-^50}'.format('BRASILEIRÃO 2021'))
print('=='*25)
print('{:-^50}'.format('TABELA DO BRASILEIRÃO'))
for pos, time in enumerate(classificacao_brasileirao_2021):
    print(f'{(pos+1):2} - {time}')
    if 'Chapecoense' in time:
        chape = pos + 1
print('=='*25)
print(f'Os 5 primeiros colocados são: {classificacao_brasileirao_2021[0:5]}')
print(f'Os 4 últimos colocados são: {classificacao_brasileirao_2021[-4:]}')
print(f'Os times em ordem alfabéticas são: {sorted(classificacao_brasileirao_2021)}')
print(f'O time da Chapecoense está na {chape}ª colocação.')
