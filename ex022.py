# crie um programa que leia o nome completo de uma pessoa e mostre:
# o nome com todas as letras maiúsculas
# o nome com todas as letras minúsculas
# quantas letras ao todo sem considerar os espaços
# quantas letras tem o primeiro nome
nome = input('Digite o seu nome completo: ').strip()
espace = nome.count(' ')
tamTot = len(nome)
print("""O seu nome em letras maiúsculas: {}.
O seu nome em letras minúsculas: {}.
Total de letras do seu nome completo: {}.
Total de letras do seu primeiro nome: {}.
""".format(nome.upper(), nome.lower(), tamTot - espace, len(nome.split()[0])))
