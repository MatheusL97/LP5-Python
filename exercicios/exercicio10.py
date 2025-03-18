# 10. Crie um algoritmo que solicite ao usuário uma idade e verifique se ela é maior ou igual a 18.

idade = int(input('Digite sua idade: '))

if idade >= 18:
    print('Voce é maior de idade')

elif idade > 0 and idade < 18:
    print('Voce é menor de idade')

else:
    print('Voce nao digitou um numero valido!')
