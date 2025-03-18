while True:
    numero = int(input('Digite um número maior que 100: '))
    
    if numero > 100:
        print('Número válido! Obrigado.')
        break
    else:
        print('Número inválido. Tente novamente.')
