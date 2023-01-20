# Faça um programa que leia o comprimento de um cateto oposto e adjacente de um triângulo retângulo
# Calcule e mostre o comprimento da hipotenusa
from math import hypot
op = float(input('Qual o comprimento do cateto oposto? Cm '))
adj = float(input('Qual o comprimento do cateto adjacente? Cm '))
print('O comprimento da hipostenusa mede: {} Cm.'.format(hypot(op, adj)))
