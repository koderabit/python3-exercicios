#Faça um programa que calcule a soma entre todos os números ímpares que são múltiplos de 3 e que se encontram dentro do intervalo entre 1 e 500
soma = 0
contagem = 0
for impares in range(1, 501, 2):
    if impares % 3 == 0:
        soma += impares
        contagem += 1
print(f'A soma dos {contagem} números ímpares que são múltiplos de três dentro do intervalo entre 1 e 500 é de {soma}.')
