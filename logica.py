# Variaveis
# String -> Str
# Int ->  inteiro
# float -> numeros flutuantes
# booleano -> bool



# -----ENTRADA E CONCATENAÇÃO-----
# nome = 'Matheus'
# idade = 28
# altura = 1.71
# bonito = True

# print(nome)
# print(type(nome))

# print(f'Meu nome é {nome}, tenho {idade} de idade, tenho a altura de {altura}.')



# ----- RECEBIMENTO DE DADOS DO USUARIO E SAIDA DE DADOS -----
# nome2 = input('Digite seu nome: ')
# print(f'Seu nome é {nome2}')



# ----- CONVERSÃO -----
# numero1 = int(input(f'Digite o primeiro numero: '))
# numero2 = int(input(f'Digite o segundo numero: '))

# soma = numero1 + numero2
# print(f'a soma dos dois numeros digitados é: {soma}')



# ----- CONDICIONAIS IF/ELIF/ELSE-----
# IF

# idade = int(input('Informe a idade: '))
# acompanhado = True

# if (idade >= 18):
#     print('voce pode assistir')

# elif (idade >=16 and idade < 18) and acompanhado == True:
#     print('voce pode assistir, pois é menor de idade e esta acompanhado.')

# elif (idade >=16 and idade < 18) and acompanhado == False:
#     print('voce pode assistir, pois é menor de idade e esta acompanhado.')

# else:
#     print('Voce nao pode assistir! Ou porque tem menos que 16 anos de idade ou não está acompanhado.')

# if idade >= 18:
#     print('Voce pode assistir')

# elif idade >= 16:
#     acompanhado = input('Esta acompanhado? S/N: ')

#     if acompanhado.lower() == 's':
#         print('Pode assistir')
#     else:
#         print('Voce nao pode assistir')

# else:
#     print('Não pode assistir, voce é menor')



# ----- CONDICIONAIS SWITCH/CASE -----

# print('Digite uma opção: ')
# print('1 - Luciano')
# print('2 - Daniel')

# opcao = int(input('Qual sua opção? '))

# match opcao:
#     case 1:
#         print('Voce escolheu o Luciano')
#     case 2:
#         print('Voce escolheu o Daniel')
#     case _:
#         print('Escolha invalida')


# ----- ESTRUTURAS DE REPETIÇÕES FOR IN RANGE -----

# for i in range(10):
#     print(i)

# frutas = ['maça', 'banana', 'uva', 'laranja']

# print(type(frutas))
# # print(frutas[2])

# for fruta in frutas:
#     print(fruta)

# # ----- ESTRUTURAS DE REPETIÇÕES WHILE -----

# #ENQUANTO

bonito = False

while bonito == False:
    resposta = input('O professor é bonito? S/N')
    
    if resposta.lower() != 's':
        print('O aluno vai tirar 0')

    else:
        print('Escolheu sabiamente')
        # bonito == True
        break
        

# while True:
#     print('O aluno vai tirar 0')

