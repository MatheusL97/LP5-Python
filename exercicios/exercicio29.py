# 29. Crie um algoritmo que pergunte ao usuário um número e verifique se ele é múltiplo de 3.

numero_1 = int(input('Digite um numero inteiro: '))

if (numero_1 % 3 == 0):
    print(f'O numero {numero_1} é multiplos de 3.')

else:
    print('O numero digitado nao é multiplo de 3.')