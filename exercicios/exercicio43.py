# 43. Desenvolva um programa que pergunte ao usuário quantas vezes ele quer que uma mensagem seja exibida, e depois use um for para imprimir essa mensagem repetidas vezes.

repeticoes = int(input('Digite a quantidade de vezes que quer repetir a frase: '))
mensagem = 'Repetindo'

for repeticao in range(repeticoes):
    repeticao += 1
    print(f'Repetindo {repeticao}x.')