# 6. Desenvolva um programa que pergunte ao usuário uma operação matemática (+, -, *, /) e dois números, e realize a operação escolhida.

operacao = input('Escolha uma operação (+, -, *, /): ')

numero1 = float(input('Digite o primeiro número: '))
numero2 = float(input('Digite o segundo número: '))

if operacao == '+':
    resultado = numero1 + numero2

elif operacao == '-':
    resultado = numero1 - numero2

elif operacao == '*':
    resultado = numero1 * numero2

elif operacao == '/':
    if numero2 != 0:
        resultado = numero1 / numero2

    else:
        resultado = "Erro! Divisão por zero."

else:
    resultado = "Operação inválida."

print(f"O resultado da operação {numero1} {operacao} {numero2} é: {resultado}")