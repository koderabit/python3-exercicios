# Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário. O programa será interrompido quando o número solicitado for negativo.

while True:
    n = int(input('Você quer ver a tabuada de qual número? '))
    print('=='*21)
    if n < 0:
        print('Tabuada finalizada...')
        break
    print(f'Tabuada de {n}:')
    for num in range(1, 11):
        print(f'{n} x {num} = {n*num}')
    print('=='*21)    
    