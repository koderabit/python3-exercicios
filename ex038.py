# Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem: O primeiro valor é maior, O segundo valor é maior ou Não existe valor maior, os dois são iguais

num1 = int(input('Digite um número inteiro: '))
num2 = int(input('Digite outro número inteiro: '))

if num1 > num2:
    print(f'O primeiro número é maior.')
elif num1 < num2:
    print(f'O segundo número é maior.')
else:
    print('Não existe valor maior, ambos os números são iguais.')
