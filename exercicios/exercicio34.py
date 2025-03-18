# 34. Escreva um programa que peça ao usuário um número e verifique se ele é positivo, negativo ou zero.

numero_digitado = input('Digite um numero inteiro, podendo se positivo, negativo ou zero: ')

if '-' in numero_digitado :
    print('Voce digitou um numero negativo')

elif numero_digitado != '0':
    print('Voce digitou um numero positivo')

else:
    numero_digitado = int(numero_digitado)
    if numero_digitado == 0:
        print('Voce digitou 0')

