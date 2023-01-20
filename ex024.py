# crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "SANTO"
cidade = input('Digite o nome de uma cidade qualquer: ').strip().upper()
if cidade.split()[0] == 'SANTO':
    resp = 'sim'
else:
    resp = 'não'
print("""O nome da cidade começa com a palavra Santo?
Resposta: {}!""".format(resp.title()))
