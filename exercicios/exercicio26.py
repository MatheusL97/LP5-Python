# 26. Desenvolva um algoritmo que peça ao usuário para inserir dois números e verifique se ambos são múltiplos de 5.

numero_1 = int(input('Digite um numero inteiro: '))
numero_2 = int(input('Digite outro numero inteiro: '))

if (numero_1 % 5 == 0) and (numero_2 % 5 == 0):
    print('Os dois numeros digitados são multiplos de 5.')

else:
    print('Um ou ambos os numeros não sao multiplos de 5')