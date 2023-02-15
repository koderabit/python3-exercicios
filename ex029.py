#Escreva um programa que leia a velocidade de um carro.
#Faça o programa mostrar uma mensagem de multa se a velocidade for maior que 80km/h.
#A multa vai custar R$ 7,00 por km acima do limite
vel = float(input("Digite a velocidade do carro em Km/h: "))
if(vel>80):
    print("Você foi multado por excesso de velocidade e deve pagar um total de R$ {:.2f}.".format((vel-80)*7))
print("Dirija com segurança!")
