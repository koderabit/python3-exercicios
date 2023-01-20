# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
from math import sin, cos, tan, radians
a = int(input('Digite o valor de um ângulo qualquer: º '))
print('O ângulo de {}º possui o seno de {:.2f}, cosseno de {:.2f} e a sua tangente vale {:.2f}.'.format(a, sin(radians(a)), cos(radians(a)), tan(radians(a))))
