# 65. Escreva um programa que solicite ao usuário uma lista de 5 números e exiba o maior e o menor número dessa lista.

numeros = []

for i in range(5):
    numero = float(input(f'Digite o {i+1}º número: '))
    numeros.append(numero)  

maior_numero = max(numeros)
menor_numero = min(numeros)

print('O maior número da lista é:', maior_numero)
print('O menor número da lista é:', menor_numero)
