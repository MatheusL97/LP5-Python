# 51. Crie um programa que peça ao usuário para inserir números até que ele digite o número 0. Ao final, exiba a soma de todos os números inseridos (exceto o 0).

soma = 0

while True:
    numero = int(input('Digite um número (ou 0 para sair): '))
    
    if numero == 0:
        break  
    
    soma += numero  

print('A soma dos números inseridos é:', soma)
