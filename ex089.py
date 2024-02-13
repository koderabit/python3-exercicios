#Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.
listaTemp = []
listaAlunosNotas = []
while True:
    nome = str(input('Digite o nome do aluno: ')).title().strip()
    nota1 = float(input(f'Digite a nota da primeira avaliação de {nome}: '))
    nota2 = float(input(f'Digite a nota da segunda avaliação de {nome}: '))
    media = (nota1 + nota2) / 2
    nota1Format = f'{nota1:.2f}'
    nota2Format = f'{nota2:.2f}'
    mediaFormat = f'{media:.2f}'
    print('--'*30)
    opcao = str(input('Você deseja cadastrar a nota de mais um aluno? [S/N] '))
    print('--'*30)
    listaTemp.append(nome)
    listaTemp.append(nota1Format)
    listaTemp.append(nota2Format)
    listaTemp.append(mediaFormat)
    listaAlunosNotas.append(listaTemp[:])
    listaTemp.clear()
    while opcao not in 'sSnN':
        opcao = str(input('Opção inválida... Você deseja cadastrar a nota de mais um aluno? [S/N] '))
        print('--'*33)
    if opcao in 'nN':
        break
print(f'{' BOLETIM GERAL ':=^66}')
print(f'{'MAT-ALUNO':<21}{'NOTA 1':<15}{'NOTA 2':<15}{'MÉDIA':<15}')
for linha in range(0, len(listaAlunosNotas)):
    print(f'{linha+1:0>3d}-',end='')
    for coluna in range(0, 4):
        if coluna == 0:
            print(f'{(listaAlunosNotas[linha][coluna]):<17}', end='')
        else:
            print(f'{(listaAlunosNotas[linha][coluna]):<15}', end='')
    print()
print('=='*33)
while True:
    print()
    mat = int(input('Digite o número da matrícula para ver a nota individual do aluno (aperte 0 para cancelar): '))
    while mat > len(listaAlunosNotas):
        mat = int(input('Matrícula inválida, digite novamente: '))
    if mat == 0:
        break
    for i in range(0, len(listaAlunosNotas)):
        if mat == i + 1:
            print('=='*33)
            print(f'{'MAT-ALUNO':<21}{'NOTA 1':<15}{'NOTA 2':<15}{'MÉDIA':<15}')
            print(f'{mat:0>3d}-{(listaAlunosNotas[i][0]):<17}{(listaAlunosNotas[i][1]):<15}{(listaAlunosNotas[i][2]):<15}{(listaAlunosNotas[i][3]):<15}')
            
print('=='*33)
