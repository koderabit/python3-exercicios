# Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele.
# Lendo o nome deles e escrevendo o nome do escolhido.
from random import choice
a1 = input('Primeiro aluno: ')
a2 = input('Segundo aluno: ')
a3 = input('Terceiro aluno: ')
a4 = input('Quarto aluno: ')
alunos = [a1, a2, a3, a4]
print('O aluno escolhido para apagar o quadro hoje foi: {}!!!'.format(choice(alunos).upper()))
