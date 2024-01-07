#escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual a base numérica para conversão. Sendo 1 para binário, 2 para octal e 3 para hexadecimal.

numero = int(input('Digite um número inteiro qualquer: '))
base = int(input('Escolha a base numérica para conversão: \nDgite 1 para base converter para base binária.\nDigite 2 para converter para base octal.\nDigite 3 para converter para base hexadecimal.\n')) 
if base == 1:
    print(f'O número {numero} convertido para base binária é: {bin(numero)[2:]}.')
elif base == 2:
    print(f'O número {numero} convertido para base octal é: {oct(numero)[2:]}.')
elif base == 3:
    print(f'O número {numero} convertido para base hexadecimal é: {hex(numero)[2:]}.')
else:
    print('Opção inválida, tente novamente.')