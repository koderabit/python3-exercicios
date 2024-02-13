#Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário. No final, mostre o conteúdo da estrutura na tela.
dados = {}
dados['nome'] = input('Digite o nome do aluno: ')
dados['media'] = float(input(f'Digite a média de {dados["nome"]}: '))
if dados['media'] >= 7:
    dados['situacao'] = 'APROVADO'
else:
    dados['situacao'] = 'REPROVADO'

print(f'O nome do aluno é {dados["nome"].title()}, a sua média foi de {dados["media"]} e portanto {dados["nome"].title()} está {dados["situacao"]}.')
