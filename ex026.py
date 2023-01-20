# faça um programa que leia uma frase pelo teclado e mostre:
# quantas vezes aparece a letra "A";
# em que posição ela aparece na primeira vez;
# em que posição ela aparece na última vez;
frase = input('Digite uma frase qualquer: ').strip().upper()
print("""o número de vezes que aparece a letra 'A' na sua frase é: {}.
A primeira vez que ela aparece é na posição {} e a última é na posição {}.
""".format(frase.count('A'), frase.find('A'), frase.rfind('A')))
