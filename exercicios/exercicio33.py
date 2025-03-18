# 33. Cr;ie um programa que solicite ao usuário o valor de um produto e calcule o desconto de 10%.

valor_produto = float(input('Digite o valor do produto: '))
valor_produto_com_desconto = valor_produto - (valor_produto * 0.1) 

print(f'O produto de {valor_produto}, com desconto de 10%, fica {valor_produto_com_desconto}')