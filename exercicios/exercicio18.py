# 18. Faça um programa que peça ao usuário três números e verifique se todos são positivos.

numero1 = float(input('Digite o primeiro número: '))
numero2 = float(input('Digite o segundo número: '))
numero3 = float(input('Digite o terceiro número: '))

if numero1 > 0 and numero2 > 0 and numero3 > 0:
    print('Todos os números são positivos.')

else:
    print('Nem todos os números são positivos.')
