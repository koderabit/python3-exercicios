#Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida: Média abaixo de 5.0: REPROVADO; Média entre 5.0 e 6.9: RECUPERAÇÃO; Média 7.0 ou superior: APROVADO
print("\033[0m")
aluno = input('Digite o nome do aluno(a): ').capitalize().strip()
nota1 = float(input(f'Digite a nota da primeira avaliação de {aluno}: '))
nota2 = float(input(f'Digite a nota da segunda avaliação de {aluno}: '))

media = (nota1 + nota2) / 2

if 0 <= nota1 <= 10 and 0 <= nota2 <= 10:
    if media < 5:
        print(f'\033[91mREPROVADO! Média: {media:.2f}')
    elif 5.0 <= media < 7.0:
        print(f'\033[93mEM RECUPERAÇÃO. Média: {media:.2f}')
    else:
        print(f'\033[92mAPROVADO! Média: {media:.2f}')

            
else:
    print('\033[93mUma ou mais notas inválidas, tente novamente.')
print("\033[0m")