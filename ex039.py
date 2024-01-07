#Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
from datetime import datetime

ano_atual = datetime.now().year

data_nascimento = int(input('Digite o seu ano de nascimento: '))

if (ano_atual - data_nascimento) < 18:
    if (data_nascimento + 18 - ano_atual) == 1:
        print('Ainda falta 1 ano para o seu alistamento militar obrigatório.')
    else:
        print(f'Ainda faltam {data_nascimento + 18 - ano_atual} anos para o seu alistamento militar obrigatório.')
elif (ano_atual - data_nascimento) > 18:
    print(f'O ano do seu alistamento militar obrigatório foi em {data_nascimento + 18}. Caso você não tenha se alistado, procure uma junta militar pois o seu alistamento está atrasado.')
else:
    print('Você está no seu ano de alistamento, procure uma junta militar para obter melhores informações.')