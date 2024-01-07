#Faça um programa que leia um número inteiro e diga se ele é ou não um número primo
numero = int(input('Digite um número inteiro: '))
primo = 0
for n in range(2, numero):
    if numero % n == 0:
        primo += 1
if primo != 0 or numero == 1:
    print(f'O número {numero} não é primo.')
else:
    print(f'O número {numero} é primo.')   
