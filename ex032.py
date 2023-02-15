#Faça um programa que pergunte um ano qualquer e mostre na tela se ele é um ano bissexto.
ano = int(input("Se você tem dúvidas se um determinado ano é bissexto, basta informá-lo e eu responderei: "))
if(ano%4==0 and ano%100!=0):
    print("É um ano Bissexto.")
elif(ano%4!=0 and ano%400==0):
    print(("É um ano Bissexto."))
else:
    print("Não é um ano Bissexto.")
