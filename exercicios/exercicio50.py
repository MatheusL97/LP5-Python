# 50. Crie um programa que peça ao usuário para inserir um número e, em seguida, exiba os números de 1 até esse número, mas de forma decrescente.

numero = int(input('Digite um número: '))

for i in range(numero, 0, -1):
    print(i)
