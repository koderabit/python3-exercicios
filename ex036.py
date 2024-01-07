#Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. A prestação não poder ser maior do que 30% do salário, senão o empréstimo será negado.

print("\033[0m")
casa = float(input('Digite o valor da casa: R$ '))
salario = float(input('Qual o salário do comprador? R$ '))
ano = int(input('O pagamento será feito em quantos anos? '))

meses = ano * 12
prestacao = casa / meses

if prestacao > (salario * 0.3):
    print("\033[91mEMPRÉSTIMO NEGADO POIS O VALOR DA PRESTAÇÃO COMPROMETERIA MAIS DO QUE 30% DO SALÁRIO DO COMPRADOR.")
elif prestacao == (salario * 0.3):
    print("\033[93mEMPRÉSTIMO APROVADO, MAS DEVE-SE TER CAUTELA POIS O VALOR DA PRESTAÇÃO CORRESPONDE A EXATAMENTE 30% DO SALÁRIO DO COMPRADOR.")
else:
    print("\033[92mEMPRÉSTIMO APROVADO COM SUCESSO.")
print("\033[0m")
