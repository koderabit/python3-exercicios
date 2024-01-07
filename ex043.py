'''
Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:

– IMC abaixo de 18,5: Abaixo do Peso

– Entre 18,5 e 25: Peso Ideal

– 25 até 30: Sobrepeso

– 30 até 40: Obesidade

– Acima de 40: Obesidade Mórbida
'''
print("\033[0m")
peso = float(input('Digite o seu peso em Kg: '))
altura = float(input('Digite a sua altura em metros: '))
imc = peso / (altura ** 2)

if imc < 18.5:
    print(f'\033[93mO seu índice de massa corporal é de {imc:.2f} e isso significa que você está abaixo do peso ideal.')
elif imc < 25:
    print(f'\033[92mO seu índice de massa corporal é de {imc:.2f} e isso significa que você está dentro do que se considera como um peso ideal.')
elif imc < 30:
    print(f'\033[93mO seu índice de massa corporal é de {imc:.2f} e isso significa que você está no quadro de sobrepeso. É bom ter cuidado.')
elif imc < 40:
    print(f'\033[38;2;255;165;0mO seu índice de massa corporal é de {imc:.2f} e isso significa que você está no quadro de obesidade. Você precisa ter atenção com isso.')
else:
    print(f'\033[91mO seu índice de massa corporal é de {imc:.2f} e isso significa que você está no quadro de Obesidade Mórbida. Você precisa de atenção urgente pois se trata de um risco alto de saúde.')
print("\033[0m")
