#Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final mostre a média de idade do grupo, qual o nome do homem mais velho e quantas pessoas do sexo feminino tem menos de 21 anos

media = 0
idade_homem_mais_velho = 0
nome_homem_mais_velho = ''
fem_21 = 0
for pessoa in range(1, 5):
    nome = input(f'Digite o nome da {pessoa}ª pessoa: ').capitalize().strip()
    idade = int(input(f'Qual a sua idade, {nome}? '))
    sexo = input('Digite o seu gênero: Masculino (M) / Feminino (F): ').lower().strip()
    print('\n')
    media += idade

    if sexo == 'm':
        if idade > idade_homem_mais_velho:
            idade_homem_mais_velho = idade
            nome_homem_mais_velho = nome 
    elif sexo == 'f':
        if idade < 21:
            fem_21 += 1
print(f'A média de idade do grupo é de {media / pessoa}, o homem mais velho é o {nome_homem_mais_velho}, de {idade_homem_mais_velho} anos e o total de pessoas do sexo feminino com menos de 21 anos é de {fem_21}.') 
