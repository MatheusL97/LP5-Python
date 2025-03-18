# 3. Desenvolva um programa que pergunte ao usuário o dia da semana (número de 1 a 7) e exiba o nome do dia correspondente.

dia_da_semana = input('Digite o dia da semana em numeros, sendo de 1 a 7: ')
dia_da_semana_int = int(dia_da_semana)

if dia_da_semana_int == 1:
    print(f'voce digitou {dia_da_semana_int}, que corresponde á Domingo.')

elif dia_da_semana_int == 2:
    print(f'voce digitou {dia_da_semana_int}, que corresponde á Segunda-Feira.')

elif dia_da_semana_int == 3:
    print(f'voce digitou {dia_da_semana_int}, que corresponde á Terça-Feira')

elif dia_da_semana_int == 4:
    print(f'voce digitou {dia_da_semana_int}, que corresponde á Quarta-Feira')

elif dia_da_semana_int == 5:
    print(f'voce digitou {dia_da_semana_int}, que corresponde á Quinta-Feira')

elif dia_da_semana_int == 6:
    print(f'voce digitou {dia_da_semana_int}, que corresponde á Sexta-Feira')

elif dia_da_semana_int == 7:
    print(f'voce digitou {dia_da_semana_int}, que corresponde á Sabádo')

else:
    print('Voce não digitou um numero de 1 á 7!')