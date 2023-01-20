# crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome
nome = input('Digite o seu nome completo: ').strip().upper()
if 'SILVA' in nome:
    resp = 'Sim'
else:
    resp = 'Não'
print("""Tem 'Silva' em algum lugar do seu nome?
Resposta: {}!
""".format(resp))
