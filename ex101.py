# Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa, retornando um valor literal indicando se uma  pessoa tem voto NEGADO, OPCIONAL ou OBRIGATÓRIO nas eleições.
from datetime import datetime
idade = 0
def voto(nascimento):
    global idade
    anoAtual = datetime.now().year
    idade = anoAtual - nascimento
    if idade <= 18:
        return 'NEGADO'
    elif idade < 65:
        return 'OBRIGATÓRIO'
    else:
        return 'OPCIONAL'


nascimento = int(input("Digite o ano do seu nascimento: "))
voto(nascimento)
print(f'IDADE: {idade} anos')
print(f'VOTO: {voto(nascimento)}')




