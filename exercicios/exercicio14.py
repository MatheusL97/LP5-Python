# 14. Desenvolva um algoritmo que peça ao usuário para digitar dois números e verifique se a soma deles é maior que 100.

numero_1 = float(input('Digite um numero: '))
numero_2 = float(input('Digite outro numero: '))

soma = numero_1 + numero_2

if soma > 100:
    print('O numero digitado é maior que 100!')

else:
    print('O numero digitado é menor que 100!')