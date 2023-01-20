# Crie um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e as suas informações possíveis.
var = input('Digite qualquer coisa: ')
print('Tipo primitivo: {}.'.format(type(var)))
print('O conteúdo é somente letras? ', var.isalpha())
print('O conteúdo é numérico? ', var.isnumeric())
print('O conteúdo é alfanumérico? ', var.isalnum())
print('O conteúdo está com letras maiúsculas? ', var.isupper())
print('O conteúdo está com letras minúsculas? ', var.islower())
print('O conteúdo está capitalizado? ', var.istitle())
