# 49. Desenvolva um programa que peça ao usuário para inserir 7 números e, ao final, exiba quantos desses números são maiores que 10.

numeros_maiores_que_10 = 0

for i in range(7):
    numero = float(input(f'Digite o {i+1}º número: '))
    
    if numero > 10:
        contador_maiores_que_10 += 1

print(f'Existem {numeros_maiores_que_10} números maiores que 10.')
