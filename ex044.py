'''
Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:

– à vista dinheiro/cheque: 10% de desconto

– à vista no cartão: 5% de desconto

– em até 2x no cartão: preço normal 

– 3x ou mais no cartão: 20% de juros
'''


preco = float(input('Digite o preço do produto: '))

print('''
Selecione a forma de pagamento:
[1] - Dinheiro / Débito / Cheque
[2] - Crédito à vista
[3] - Crédito parcelado até 2x
[4] - Crédito parcelado - 3x ou mais 

''')

opcao = int(input('Forma de pagamento: '))

if opcao == 1:
    print(f'Na opção de pagamento escolhida o valor do produto ganha 10% de desconto e fica por R$ {(preco * 0.9):.2f}')
elif opcao == 2:
    print(f'Na opção de pagamento escolhida o valor do produto ganha 5% de desconto e fica por R$ {(preco * 0.95):.2f}')
elif opcao == 3:
    print(f'Na opção de pagamento escolhida o valor do produto não sofre ajuste e permanece R$ {(preco):.2f}')
elif opcao == 4:
    print(f'Na opção de pagamento escolhida o valor do produto ganha 20% de juros e fica por R$ {(preco * 1.2):.2f}')
else:
    print('Opção de pagamento inválida, tente novamente.')
