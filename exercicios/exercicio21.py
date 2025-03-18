# 21. Escreva um algoritmo que peça ao usuário para digitar um número e verifique se ele é maior, menor ou igual a 10.

numero_digitado = float(input('Digite um numero: '))

if numero_digitado > 10:
    print('O numero digitado é maior que 10.')

elif numero_digitado < 10:
    print('O numero digitado é menor que 10.')

elif numero_digitado == 10:
    print('O numero digitado é igual que 10.') 

else:
    print('Voce nao digitou um numero valido!')
