#Crie um programa que leia um número inteiro qualquer e mostre o seu fatorial.
n = int(input('Digite um número inteiro qualquer: '))
c = n
fat = 1 
print(f'Calculando o fatorial de {n}!: ', end='')
while c > 0:
    print(f'{c}', end='')
    print(' x ' if c > 1 else ' = ', end='')
    fat *= c
    c-=1
print(f'{fat}.')
