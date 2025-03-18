# 53. Escreva um programa que peça ao usuário um número e exiba a contagem regressiva desse número até 1.

numero = int(input('Digite um número para iniciar a contagem regressiva: '))

for i in range(numero, 0, -1):
    print(i)
