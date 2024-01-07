#desenvolva um programa que leia seis números inteiros e mostre a soma de todos os que forem pares, os números que forem ímpares, desconsidere.
soma = 0
pares = 0
for num in range(1, 7):
    n = int(input(f'Digite o {num}° número inteiro: '))
    if n % 2 == 0:
        soma += n
        pares += 1
print(f'A soma dos {pares} números pares lidos anteriormente vale {soma}.')
