# 17. Crie um programa que solicite ao usuário dois números e exiba a soma, subtração, multiplicação e divisão entre eles.

numero1 = float(input('Digite o primeiro número: '))
numero2 = float(input('Digite o segundo número: '))

soma = numero1 + numero2
subtracao = numero1 - numero2
multiplicacao = numero1 * numero2

if numero2 != 0:
    divisao = numero1 / numero2

else:
    divisao = 'Indefinido (divisão por zero)'

print(f'A soma entre {numero1} e {numero2} é: {soma}')
print(f'A subtração entre {numero1} e {numero2} é: {subtracao}')
print(f'A multiplicação entre {numero1} e {numero2} é: {multiplicacao}')
print(f'A divisão entre {numero1} e {numero2} é: {divisao}')
