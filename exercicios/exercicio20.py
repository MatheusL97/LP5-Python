# 20. Crie um programa que solicite ao usuário a temperatura em graus Celsius e converta para Fahrenheit.


celsius = float(input('Digite a temperatura em graus Celsius: '))

fahrenheit = (celsius * 9/5) + 32

print(f'A temperatura de {celsius}°C corresponde a {fahrenheit}°F.')
