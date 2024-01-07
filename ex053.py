#Faça um programa que leia uma frase e diga se ela é um palíndromo, desconsiderando os espaços. Ex: "apos a sopa"
frase = input('Escreva a sua frase: ').strip().replace(' ', '').upper()
reverso = frase[::-1]

print(f'A frase {frase} invertida fica {reverso}', end=' ')

if frase == reverso:
    print('e por isso temos um palíndromo nesta frase.')
else:
    print('e por isso não temos um palíndromo nesta frase.')
