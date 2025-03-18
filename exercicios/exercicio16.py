combustivel = input('Digite o tipo de combustível (gasolina, etanol, diesel): ').lower()

if combustivel == 'gasolina':
    preco = 5.79 
    print(f'O preço da {combustivel} é de {preco}')

elif combustivel == 'etanol':
    preco = 4.29  
    print(f'O preço da {combustivel} é de {preco}')

elif combustivel == 'diesel':
    preco = 6.55  
    print(f'O preço da {combustivel} é de {preco}')

else:
    print('Voce nao digitou um combustivel valido!') 
    


