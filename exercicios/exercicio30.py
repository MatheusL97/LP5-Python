# 30. Faça um programa que pergunte ao usuário a idade e verifique se ele pode votar (idade maior ou igual a 16).

idade = int(input('Digite sua idade: '))
maior_idade = idade >= 16

if maior_idade:
    print('Voce ja pode votar.')

else: 
    print('Voce nao pode votar.')