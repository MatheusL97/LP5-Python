import random

numero_secreto = random.randint(1, 10)

while True:
    palpite = int(input('Adivinhe o número secreto entre 1 e 10: '))
    
    if palpite == numero_secreto:
        print('Parabéns! Você adivinhou o número secreto!')
        break  
    else:
        print('Errado! Tente novamente.')
