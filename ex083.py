# Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.
expressao = input('Digite uma expressão matemática que contenha parênteses: ').strip()
pilha = []
for letra in expressao:
    if letra == '(':
        pilha.append('(')
    elif letra == (')'):
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) > 0:
    print('Expressão digitada incorretamente')
else:
    print('Expressão digitada corretamente.')
