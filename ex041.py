# Define categorias de atletas de acordo com a idade: MIRIM até 9 anos, INFANTIL até 14 anos, JÚNIOR até 19 anos, SÊNIOR até 25 anos, MASTER acima de 25 anos
atleta = input('Qual o nome do(a) atleta? ').capitalize().strip()
idade = int(input('Qual a idade do atleta? '))

if idade > 0:
    if idade <= 9:
        print(f'O(a) atleta {atleta} está na categoria MIRIM.')
    elif idade <= 14:
        print(f'O(a) atleta {atleta} está na categoria INFANTIL.')
    elif idade <= 19:
        print(f'O(a) atleta {atleta} está na categoria JÚNIOR.')
    elif idade <= 25:
        print(f'O(a) atleta {atleta} está na categoria SÊNIOR.')
    elif idade > 25:
        print(f'O(a) atleta {atleta} está na categoria MASTER.')
else: 
    print('Idade inválida, tente novamente.')