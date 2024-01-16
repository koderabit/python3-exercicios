#Crieum programa que leia dois valores e mostre um menu na tela: 1-Somar, 2-Multiplicar, 3-Maior, 4-Novos números, 5-sair do programa. Seu programa deverá realizar a operação de acordo com a escolha.
valor1 = int(input('Digite o primeiro valor: '))
valor2 = int(input('Digite o segundo valor: '))
opcao = 0
while opcao != 5:
    print('#=#='*20)
    opcao = int(input('''\n[1] - SOMAR\n[2] - MULTIPLICAR\n[3] - MAIOR ENTRE ELES\n[4] - ESCOLHER NOVOS VALORES\n[5] - SAIR\nEsolha uma das opções: '''))
    print('#=#='*20)
    if opcao == 1:
        print(f'A soma entre {valor1} + {valor2} = {valor1 + valor2}.')
    elif opcao == 2:
        print(f'A multiplicação entre {valor1} x {valor2} = {valor1 * valor2}.')
    elif opcao == 3:
        if valor1 > valor2:
           maior = valor1
           print(f'O maior número entre {valor1} e {valor2} é o número {maior}.')
        else:
            maior = valor2
            print(f'O maior número entre {valor1} e {valor2} é o número {maior}.')
    elif opcao == 4:
        valor1 = int(input('Digite o primeiro valor: '))
        valor2 = int(input('Digite o segundo valor: '))
    elif opcao == 5:
        break
    else:
        print('Opção inválida, tente novamente.')

msgFinal = ('finalizando...')
from time import sleep
for letras in msgFinal:
    print(letras, end='', flush=True)
    sleep(0.05)
