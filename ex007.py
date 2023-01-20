# Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.
aluno = input('Qual o nome do aluno? ')
n1 = float(input('Qual a nota da primeira avaliação de {}? '.format(aluno)))
n2 = float(input('Qual a nota da segunda avaliação de {}? '.format(aluno)))
print('A média geral de {} foi {:.2f}.'.format(aluno, (n1+n2)/2))
