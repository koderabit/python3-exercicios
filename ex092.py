#Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade) em um dicionário. Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário. Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.
from datetime import datetime
ano_atual = datetime.now().year
cadastro = dict()
cadastro['nome'] = input('DIGITE O NOME DO CIDADÃO: ').upper().strip()
ano_nascimento = int(input(f'DIGITE O ANO DE NASCIMENTO DE {cadastro["nome"]}: '))
cadastro['idade'] = ano_atual - ano_nascimento
cadastro['ctps'] = input(f'DIGITE O Nº DA CTPS DE {cadastro["nome"]} [DIGITE 0 SE NÃO POSSUI]: ').upper().strip()
if cadastro['ctps'] != '0':
    cadastro['ano de contratacao'] = int(input(f'DIGITE O ANO DE CONTRATAÇÃO DE {cadastro["nome"]}: '))
    cadastro['salário'] = float(input(f'QUAL O SALÁRIO DE {cadastro["nome"]}? R$ '))
    cadastro[f'idade para {cadastro["nome"]} se aposentar'] = cadastro['ano de contratacao'] - ano_nascimento + 35
print()
print(f'{'CADASTRO DE TRABALHADOR':*^50}')
for k, v in cadastro.items():
    print(f'{k.upper():-<30}{v:->20}')
print('*'*50)