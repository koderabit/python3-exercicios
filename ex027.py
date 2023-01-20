# faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o últio nome separadamente;
nome = input('Digite o seu nome completo: ').strip()
print("""Primeiro nome: {}.
Último nome: {}.""".format(nome.split()[0].title(), nome.split()[-1].title()))
