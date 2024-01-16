# Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
# A) Quantas vezes apareceu o valor 9.
# B) Em que posição foi digitado o primeiro valor 3.
# C) Quais foram os números pares.
numeros = (int(input('Digite um número inteiro: ')), int(input('Digite outro número inteiro: ')), int(input('Digite outro número inteiro: ')), int(input('Digite outro número inteiro: ')))
print(f'O número 9 apareceu {numeros.count(9)} vezes.')
if 3 in numeros:
    print(f'O número 3 foi encontrado pela primeira vez na posição {numeros.index(3)}.')
else:
    print('Não foi encontrado nenhum número 3.')
print(f'Números pares na tupla: ', end='')
for numero in numeros:
    if numero % 2 == 0:
        print(numero, end=' ')
