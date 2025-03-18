# 46. Desenvolva um programa que pergunte ao usuário para inserir 10 números e, ao final, exiba a média dos números inseridos.


soma = 0

for i in range(10):
    numero = float(input(f'Digite o {i+1}º número: '))
    soma += numero  

media = soma / 10

print('A média dos números inseridos é:', media)
