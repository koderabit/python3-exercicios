''' 
Refaça o DESAFIO 35 dos triângulos, mostrando o tipo de triângulo que será formado: 
 - EQUILÁTERO: todos os lados iguais
 - ISÓSCELES: dois lados iguais, um diferente
 - ESCALENO: todos os lados diferentes '''

r1 = float(input('Digite o comprimento de um seguimento de reta qualquer em Cm: '))
r2 = float(input('Digite outro comprimento de um seguimento de reta qualquer em Cm: '))
r3 = float(input('Digite mais um comprimento de um seguimento de reta qualquer em Cm: '))
if(r1 + r2 <= r3 or r1 + r3 <= r2 or r2 + r3 <= r1):
    print('Não é possível formar um triângulo com os seguimentos de reta informados.')
else:
    if r1 == r2 or r1 == r3 or r2 ==r3:
        if r1 == r2 == r3:
            print('Com os seguimentos de reta informados é possível formar um triângulo equilátero.')
        else:
            print('Com os seguimentos de reta informados é possível formar um triângulo isósceles.')
        
    else:
        print('Com os seguimentos de reta informados é possível formar um triângulo escaleno.')