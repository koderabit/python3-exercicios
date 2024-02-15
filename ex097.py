# Faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer como parâmetro e mostre uma mensagem com tamanho adaptável.  
def escreva(msg):
    tam = len(msg) + 2
    print('=' * tam)
    print(f'|{msg}|')
    print('=' * tam)


escreva('KODERABIT - APROXIMANDO TECNOLOGIA E PESSOAS')
