# 28. Escreva um programa que peça ao usuário para inserir uma palavra e verifique se ela tem mais de 5 letras.

palavra_digitada = input('Dgite uma palavra: ')

if len(palavra_digitada) > 5:
    print('A palavra digitada tem mais de 5 letras.')

else:
    print('A palavra digitada tem menos que 5 letras.')
