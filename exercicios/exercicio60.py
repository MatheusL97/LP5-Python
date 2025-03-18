# 60. Crie um programa que peça ao usuário um número e exiba todos os divisores desse número.

numero = int(input('Digite um número para ver seus divisores: '))

print(f'Divisores de {numero}:')
for i in range(1, numero + 1):
    if numero % i == 0:
        print(i)
