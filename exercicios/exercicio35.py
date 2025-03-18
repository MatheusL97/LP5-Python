# 35. Desenvolva um algoritmo que peça ao usuário para digitar dois números e verifique se a multiplicação deles é igual a 20.

numero_1 = int(input('Digite o primeiro numero:'))
numero_2 = int(input('Digite o segundo numero:'))
multiplicacao_numeros = numero_1 * numero_2

if multiplicacao_numeros == 20:
    print('A multiplicação dos numeros é igual a 20.')

else:
    print('A multiplicação dos numeros não é igual a 20')