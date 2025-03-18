# 22. Escreva um programa que peça ao usuário para inserir dois números e verifique se o primeiro é maior que o segundo.

numero_1 = float(input('Digite um numero: '))
numero_2 = float(input('Digite outro numero: '))

if numero_1 > numero_2:
    print(f'O numero {numero_1} é maior que o numero {numero_2}')

else:
    print(f'O numero {numero_2} é maior que o numero {numero_1}')
