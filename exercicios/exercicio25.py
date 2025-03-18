# 25. Escreva um programa que peça ao usuário um número de 0 a 20 e verifique se ele está entre 10 e 15.

numero_digitado = int(input('Digite um numero de 0 a 20: '))

if numero_digitado > 9 and numero_digitado < 16:
    print(f'O numero {numero_digitado} está entre 10 e 15.')

else:
    print(f'O numero {numero_digitado} não está entre 10 e 15.')
