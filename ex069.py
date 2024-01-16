# Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
# A) quantas pessoas tem mais de 18 anos.
# B) quantos homens foram cadastrados.
# C) quantas mulheres tem menos de 20 anos.
print('=='*22)
print('CADASTRO GERAL DE USUÁRIOS -> IDADE/SEXO...')
print('=='*22)

maiorIdade = homens = mulheresAbaixo20 = 0
while True:
    idade = int(input('Digite a idade do usuário: '))
    sexo = input('Digite o sexo do usuário: [M/F]: ').strip()[0]
    while sexo not in 'fFmM':
        sexo = input('Digite o sexo do usuário: [M/F]: ').strip()[0]
    print('=='*22)
    if idade > 18:
        maiorIdade += 1
    if sexo in 'mM':
        homens += 1
    if idade < 20 and sexo in 'fF':
        mulheresAbaixo20 += 1
    print('Usuário cadastrado com sucesso...')
    continuar = input('Deseja cadastrar mais usuários? [S/N]: ').strip()[0]
    while continuar not in 'sSnN':
        continuar = input('Deseja cadastrar mais usuários? [S/N]: ').strip()[0]
    if continuar in 'nN':
        print('=='*22)
        break
    print('=='*22)
print(f'''Número total de pessoas cadastradas com idade superior a 18 anos: {maiorIdade}.
Número total de homens cadastrados: {homens}.
Número total de mulheres cadastradas com idade inferior a 20 anos: {mulheresAbaixo20}.''')
