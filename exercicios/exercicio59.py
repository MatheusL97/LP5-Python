# 59. Escreva um programa que solicite ao usuário para digitar dois números e verifique se o primeiro é maior que o segundo. Continue pedindo números até que o primeiro número seja maior que o segundo.

while True:
    primeiro_numero = float(input('Digite o primeiro número: '))
    segundo_numero = float(input('Digite o segundo número: '))
    
    if primeiro_numero > segundo_numero:
        print('O primeiro número é maior que o segundo.')
        break  
    else:
        print('O primeiro número não é maior que o segundo. Tente novamente.')
