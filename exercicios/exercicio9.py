# 9. Crie um algoritmo que verifique se um número inserido pelo usuário é par ou ímpar.

numero_digitado = int(input('Digite um numero inteiro: '))


if numero_digitado <= 0:
    print(f'{numero_digitado} não é valido!')

elif numero_digitado % 2 == 0:
    print(f'{numero_digitado} é par!')

else:
    print(f'{numero_digitado} é impar!')
