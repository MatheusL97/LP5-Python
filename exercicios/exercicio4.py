# 4. Crie um algoritmo que solicite ao usuário uma cor (vermelho, verde, azul) e exiba uma mensagem correspondente à cor escolhida.

cor_digitada = input('Escolha uma das cores: Vermelho, Azul ou Verde: ').lower()

if cor_digitada == 'vermelho':
    print('Voce escolheu Vermelho.')

elif cor_digitada == 'azul':
    print('Voce escolheu Azul.')

elif cor_digitada == 'verde':
    print('Voce escolheu Verde.')

else:
    print('Voce não escolheu nenhuma das cores!')