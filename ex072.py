# Crie um programa que tenha uma dupla totalmente preenchida com uma contagem por extenso, de zero até vinte. Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.
numeros = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze', 'Treze', 'Quatorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')

while True:
    numero = int(input('Escolha um número entre 0 e 20: '))
    if numero < 0 or numero > 20:
        numero = int(input('Tente novamente... Escolha um número entre 0 e 20: '))
    print(f'O número escolhido foi: {numeros[numero]}.')
    continuar = input(('Você deseja continuar? [S/N]: '))
    if continuar in 'sS':
        continue
    else:
        break