#Escreva um programa que leia um número N inteiro qualquer e mostre na tela os N primeiros elementos de uma Sequência de Fibonacci. Exemplo: 0 – 1 – 1 – 2 – 3 – 5 – 8
print('~~'*12)
print('Sequência de Fibonacci')
print('~~'*12)
termos = int(input('Quantos termos você deseja mostrar: '))
cont = 3
n1 = 0
n2 = 1
print('0 >>>> 1 >>>> 1', end=' >>>> ')
while cont < termos:
    atual = n1 + n2 # atual = 1
    n1 = n2 # n1 = 1
    n2 = atual # n2 = 1
    atual = n2 + n1 # atual = 2
    print(atual, end=' >>>> ')
    cont+=1
print('FIM')
