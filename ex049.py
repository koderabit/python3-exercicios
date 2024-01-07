#Refaça o desafio do exercício 009, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando o laço for.
from time import sleep
n = int(input('Digite um número inteiro: '))
print(f'Tabuada de {n}:')
for num in range(1, 11):
    print(f'{n} x {num:2} = {n * num}')
    sleep(0.05)