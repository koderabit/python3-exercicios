# Escreva um programa que leia um valor em metros e escreva ele convertido em centímetros e milímetros.
d = float(input('Digite uma distância em metros: '))
print('*-*'*25)
print('A distância de {:.2f}m, convertida em cm vale {:.2f}cm e em mm vale {:.2f}mm.'.format(d, d*100, d*1000))
print('*-*'*25)
