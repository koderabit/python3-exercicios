#Crie um programa que leia um número inteiro qualquer e mostre na tela se o número é par ou ímpar.
n = int(input("Digite um número inteiro qualquer: "))
if(n%2==0):
    print("O número {} é par.".format(n))
else:
    print("O número {} é ímpar.".format(n))
