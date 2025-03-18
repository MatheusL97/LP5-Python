# 15. Escreva um programa que pergunte ao usuário uma idade e verifique se a pessoa é adolescente (entre 13 e 17 anos).


idade = int(input('Digite sua idade: '))

if 13 <= idade <= 17:
    print('Você é um adolescente.')

else:
    print('Você não é um adolescente.')

