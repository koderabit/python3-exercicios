# Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues. OBS: considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.
print('##'*15)
print('{:-^30}'.format('KODERABIT BANKING'))
print('##'*15)

ced = 50
totalCed = 0
saque = int(input('Quanto você deseja sacar? R$ '))
saldo = saque
while True:
    if saldo >= ced:
        saldo -= ced
        totalCed += 1
    else:
        if totalCed > 0:
            print(f'Total de {totalCed} de R${ced},00.')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totalCed = 0
        if saldo == 0:
            break
