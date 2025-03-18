# 2. Escreva um programa que peça ao usuário para inserir um número e verifique se o número é maior que 10.

numero_digitado = input('Digite um numero: ')
numero_digitado_float = float(numero_digitado)

if numero_digitado_float > 10:
    print('O numero que voce digitou é maior que 10.')

else:
    print('O numero que voce digitou é menor ou igual a 10.')