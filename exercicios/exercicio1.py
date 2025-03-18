# 1. Crie um programa que pergunte ao usuário um número de 1 a 3 e exiba o nome correspondente ao número (1: "um", 2: "dois", 3: "três").

numero_digitado_int = input('Digite um numero do 1 ao 3: ')
numero_digitado_int = int(numero_digitado_int)

if numero_digitado_int == 1:
    print(f'{numero_digitado_int}: Um')


elif numero_digitado_int == 2:
    print(f'{numero_digitado_int}: Dois')


elif numero_digitado_int == 3:
    print(f'{numero_digitado_int}: Três')

else:
    print('Voce nao digitou nenhum dos numeros ofertados(1, 2 ou 3)!')