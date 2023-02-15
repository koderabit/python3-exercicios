#Faça um programa que leia 3 números e mostre qual é o maior e o menor.
n1 = int(input('Digite um número inteiro qualquer: '))
n2 = int(input('Digite outro número inteiro qualquer: '))
n3 = int(input('Digite mais um número inteiro qualquer: '))
if(n1 > n2 and n1 > n3):
    maior = n1
elif(n2 > n1 and n2 > n3):
    maior = n2
else:
    maior =n3

if(n1 < n2 and n1 < n3):
    menor = n1
elif(n2 < n1 and n2 < n3):
    menor = n2
else:
    menor = n3
print('O maior número é o {} e o menor é o {}.'.format(maior, menor))
