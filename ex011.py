# Faça um programa que leia a largura e altura de uma parede em metros, calcule a área e a quantidade de tinta
# necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2m².
lar = float(input('Digite o tamanho da largura da parede em metros: '))
alt = float(input('Digie o tamanho da altura da parede em metros: '))
print('Como a área da parede é de {:.2f}m², serão necessários {:.2f}l de tinta'.format(lar*alt, lar*alt/2))
