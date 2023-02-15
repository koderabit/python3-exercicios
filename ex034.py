#Escreva um programa que leia o salário de um funcionário.
#Se o salário for maior que 1250, calcule um aumento de 10%, se for menor ou igual, aumento de 15%.
sal = float(input('Digite o valor do salário do colaborador: R$ '))
if(sal>1250):
    print('O novo salário do colaborador terá um aumento de 10% e valerá R$ {:.2f}.'.format(sal*1.1))
else:
    print('O novo salário do colaborador terá um aumento de 15% e valerá R$ {:.2f}.'.format(sal * 1.15))
