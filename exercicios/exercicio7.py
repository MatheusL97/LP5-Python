# 7. Escreva um programa que peça ao usuário uma nota de 0 a 10 e classifique a nota como "Baixa", "Média" ou "Alta" usando estrutura condicional if.

nota = float(input('Digite uma nota de 0 a 10: '))

if 0 <= nota <= 3:
    classificacao = 'Baixa'

elif 3 < nota <= 7:
    classificacao = 'Média'

elif 7 < nota <= 10:
    classificacao = 'Alta'

else:
    classificacao = 'Nota inválida! A nota deve ser entre 0 e 10.'


print(f'A classificação da nota {nota} é: {classificacao}')