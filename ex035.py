#Desenvolva um programa que leia o comprimento de 3 retas e diga se é possível formar um triângulo com elas.
r1 = float(input('Digite o comprimento de um seguimento de reta qualquer em Cm: '))
r2 = float(input('Digite outro comprimento de um seguimento de reta qualquer em Cm: '))
r3 = float(input('Digite mais um comprimento de um seguimento de reta qualquer em Cm: '))
if(r1 + r2 <= r3 or r1 + r3 <= r2 or r2 + r3 <= r1):
    print('Não é possível formar um triângulo com os seguimentos de reta informados.')
else:
    print('Com os seguimentos de reta informados é possível formar um triângulo.')