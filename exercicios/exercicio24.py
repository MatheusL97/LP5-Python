# 24. Desenvolva um algoritmo que pergunte ao usuário o nome de uma cidade e verifique se é a capital do Brasil.

cidade = input('Digite o nome de uma cidade: ').lower()

if 'df' in cidade or 'brasilia' in cidade:
    print('Voce digitou Brasilia/DF, nossa capital.')

else: 
    print('Esta cidade não é a capital.')