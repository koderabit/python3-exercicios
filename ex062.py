#Melhore o desafio 061, perguntando se o usuário deseja mostrar mais termos. O programa se encerra quando o usuário disser que quer 0 termos.
termo = int(input('Digite o valor do primeiro termo da progressão aritimética: '))
razao = int(input('Digite o valor da razão da PA: '))
qtd = 1
total = 0
mais = 10
while mais != 0:
    total += mais
    while qtd <= total:
        print(f'{termo} >>>> ', end='')
        termo += razao
        qtd +=1
    print('PAUSA')
    mais = int(input('Você gostaria de mostrar mais quantos termos da PA? '))
print(F'FIM DA PA COM {total} TERMOS.')
