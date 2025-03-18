# 5. Faça um programa que solicite ao usuário dois números e verifique se ambos são pares.

numero_1 = int(input('Digite um numero: '))
numero_2 = int(input('Digite outro numero: '))


if numero_1 == 0 or numero_2 == 0:
    print('O zero não vale!')

elif numero_1 % 2 == 0 and numero_2 % 2 == 0:
    print('Ambos os numeros digitados sao pares!')

elif numero_1 % 2 == 1 or numero_2 % 2 == 1:
    print('Um ou ambos os numeros digitados não sao pares!')



else:
    print('voce nao digitou um numero valido!')