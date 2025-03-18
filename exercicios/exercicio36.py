# 36. Crie um programa que solicite ao usuário um número de 1 a 12 e exiba o mês correspondente.

numero = int(input('Digite um número de 1 a 12: '))

meses = [
    'Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho',
    'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro'
]

if 1 <= numero <= 12:
    print(f'O mês correspondente ao número {numero} é: {meses[numero - 1]}')
else:
    print('Número inválido! Digite um número entre 1 e 12.')
