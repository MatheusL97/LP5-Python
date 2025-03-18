# 27. Crie um programa que solicite ao usuário três números e exiba o maior deles.

numero_1 = float(input('Digite o primeiro numero: '))
numero_2 = float(input('Digite o segundo numero: '))
numero_3 = float(input('Digite o terceiro numero: '))

lista_numero = [numero_1, numero_2, numero_3]
numero_maior = max(lista_numero)
print(f'O maior numero dentre os digitados foi {numero_maior}.')
