# 23. Crie um algoritmo que peça ao usuário uma palavra e verifique se a palavra é "Python".

palavra_digitada = input('Digite uma palavra: ').capitalize()
palara_chave = 'Python'

if palavra_digitada == palara_chave:
    print('Voce digitou Python, parabens!')
    
else:
    print('Voce nao digitou Python')
