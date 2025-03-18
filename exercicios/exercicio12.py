# 12. Escreva um programa que peça ao usuário para escolher um modo de transporte (carro, bicicleta, a pé) e exiba uma mensagem com a velocidade média correspondente.

transporte = input('Escolha um modo de transporte (carro, bicicleta, a pé): ').lower()

if transporte == 'carro':
    print('A velocidade média do carro é 80 km/h.')

elif transporte == 'bicicleta':
  print('A velocidade média da bicicleta é 25 km/h.')

elif transporte == 'a pe' or transporte == 'a pé':
    print('A velocidade média a pé é 5 km/h.')

else:
    print('Modo de transporte inválido. Por favor, escolha entre carro, bicicleta ou a pé.')


