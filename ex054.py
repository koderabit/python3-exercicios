#Crie um programa que leia a data de nascimento de sete pessoas, no final mostre a quantidade de pessoas que ainda não atingiram a maior idade e quantas já atingiram.
from datetime import datetime
maior = 0
menor = 0
data_atual = datetime.now()
for nascimento in range(1, 8):
    dia_nascimento = input('Digite a sua data de nascimento: ').strip()
    data_nascimento = datetime.strptime(dia_nascimento, '%d/%m/%Y')
    idade = data_atual.year - data_nascimento.year - ((data_atual.month, data_atual.day) < (data_nascimento.month, data_nascimento.day))
    if idade < 18:
        menor += 1
    else:
        maior += 1

print(f'Dentre as pessoas que preencheram suas datas de nascimento, o número de pessoas que atingiram a maior idade é igual a {maior} e o número de pessoas que ainda não atingiram a maior idade é igual a {menor}.')