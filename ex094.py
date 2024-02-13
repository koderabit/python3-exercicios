#Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista. No final, mostre: A) Quantas pessoas foram cadastradas B) A média de idade C) Uma lista com as mulheres D) Uma lista de pessoas com idade acima da média
pessoas = []
fem = []
dados = {}
idade = 0
print('=='*25)
print(f'{'KODERABIT CADASTRO':-^50}')
print('=='*25)

while True:
    dados['nome'] = input('Nome: ').strip().upper()
    while True:
        dados['sexo'] = input('Sexo [M/F]: ').strip().upper()[0]
        if dados['sexo'] in 'MF':
            break
        print('ATENÇÃO. DIGITE APENAS M OU F. ')
    dados['idade'] = int(input('Idade: '))
    print('=='*25)
    idade += dados['idade']
    pessoas.append(dados.copy())
    if dados['sexo'] == 'F':
        fem.append(dados.copy())
    opcao = input('Deseja cadastrar uma nova pessoa? [S/N] ').strip().upper()[0]
    while opcao not in 'SN':
        print('=='*25)
        opcao = input('Opção inválida. Deseja cadastrar uma nova pessoa? [S/N] ').strip().upper()[0]
        print('=='*25)
        print()
    if opcao in 'N':
        print('=='*25)
        break
print(f'Total de pessoas cadastradas: {len(pessoas)}.')
print('=='*25)
print(f'Lista feminina: ', end='')
c=0
for c in range(0, len(fem)):
    if c == len(fem) - 1:
        print(fem[c]['nome'], end='.')
    elif c == len(fem) - 2:
        print(fem[c]['nome'], end=' e ')
    else:
        print(fem[c]['nome'], end=', ')
    c += 1
print()
print('=='*25)
media_idade = idade / len(pessoas)
acima_idade = []
for p in pessoas:
    if p['idade'] > media_idade:
        acima_idade.append(p.copy())
print(f'Lista de pessoas com idade acima da média de {media_idade:.2f}: ')
for p in acima_idade:
    for k, v in p.items():
        print(f'{k}: {v}.')
    print('--'*25)
print('=='*25)
