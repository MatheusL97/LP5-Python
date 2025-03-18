# 56. Escreva um programa que pergunte ao usuário quantas vezes ele quer que uma mensagem seja exibida, e utilize um laço while para exibir a mensagem a quantidade de vezes desejada.

quantidade = int(input('Quantas vezes você quer que a mensagem seja exibida? '))

contador = 0

while contador < quantidade:
    print('Esta é a sua mensagem!')
    contador += 1  
