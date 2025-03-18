# 64. Crie uma lista com 10 números aleatórios e exiba apenas os números que são múltiplos de 3.

import random

numeros = [random.randint(1, 100) for _ in range(10)]

print('Números aleatórios:', numeros)
print('Múltiplos de 3:')
for numero in numeros:
    if numero % 3 == 0:
        print(numero)
