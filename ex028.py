#Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário
#Tentar descobrir o número escolhido e depois mostre na tela se o usuário acertou ou não.
from random import randint
numComput = randint(1, 5)
numUser = int(input("Pensei em um número inteiro de 1 a 5, aposto que você não é capaz de adivinhar, mas pode tentar: "))
if(numComput == numUser):
    print("Você acertou, por acaso vocẽ lê mente de máquinas?")
elif(numUser>5 or numUser<1):
    print("Número inválido, tente novamente!")
else:
    print("Errado, o número correto era {}. Eu avisei que você não seria capaz de descobrir".format(numComput))
