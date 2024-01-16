#Faça um programa que leia o sexo de uma pessoa mas só aceite valores M ou F. Caso esteja errado, peça para digitar novamente até ter os valores corretos.
gen = input('Digite o seu sexo: [M/F]: ').upper().strip()[0]
while gen not in 'MmFf':
    gen = input('Dados inválidos! Digite o seu sexo: [M/F]: ').upper().strip()[0]
print(f'Gênero {gen} registrado com Sucesso.')