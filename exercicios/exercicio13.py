# 13. Crie um algoritmo que solicite ao usuário um mês do ano (1 a 12) e exiba a estação do ano correspondente.

mes = int(input('Digite o número do mês (1 a 12): '))

# Verifica a estação do ano correspondente ao mês
if mes == 1 or mes == 2 or mes == 3:
    print('Verão')

elif mes == 4 or mes == 5 or mes == 6:
    print('Outono')

elif mes == 7 or mes == 8 or mes == 9:
    print('Inverno')

elif mes == 10 or mes == 11 or mes == 12:
    print('Primavera')

else:
    print('Mês inválido. Por favor, insira um número entre 1 e 12.')

