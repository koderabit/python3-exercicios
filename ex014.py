# Escreva um programa que converta uma temperatura digitada em ºC para ºF.
cel = float(input('Digite uma temperatura em ºC '))
print('A temperatura de {:.1f}ºC equivale a {:.1f}ºF na escala richter.'.format(cel, (cel * 9 / 5 + 32)))
