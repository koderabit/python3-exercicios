# Faça um algorítimo que leia o salário de um funcionário e mostre o seu novo salário com 15% de aumento.
sal = float(input('Digite o salário atual do funcionário: R$ '))
print('Devido ao reajuste salarial, o novo salário do colaborador será de R$ {:.2f}.'.format(sal*1.15))
