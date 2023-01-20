# faça um programa que leia um número de 0 a 9999 e mostre na tla cada um dos dígitos separados
num = input('Digite um número inteiro entre 1 e 9999. ').strip()
if len(num) == 1:
    milhar = centena = dezena = 0
    unidade = num
elif len(num) == 2:
    milhar = centena = 0
    dezena = num[0]
    unidade = num[1]
elif len(num) == 3:
    milhar = 0
    centena = num[0]
    dezena = num[1]
    unidade = num[2]
else:
    milhar = num[0]
    centena = num[1]
    dezena = num[2]
    unidade = num[3]
print("""Composição do número escolhido:
Milhar: {}.
Centena: {}.
Dezena: {}.
Unidade: {}.
""".format(milhar, centena, dezena, unidade))
