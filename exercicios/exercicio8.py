# 8. Desenvolva um algoritmo que pergunte ao usuário o estado civil (solteiro, casado, divorciado, viúvo) e exiba uma mensagem correspondente.

estado_civil = input('Digite seu estado civil (solteiro, casado, divorciado, viúvo): ').lower()

if estado_civil == 'solteiro':
    mensagem = 'Você está solteiro(a).'

elif estado_civil == 'casado':
    mensagem = 'Você está casado(a).'

elif estado_civil == 'divorciado':
    mensagem = 'Você está divorciado(a).'

elif estado_civil == 'viúvo':
    mensagem = 'Você está viúvo(a).'

else:
    mensagem = 'Estado civil inválido. Por favor, insira um estado civil válido (solteiro, casado, divorciado, viúvo).'

print(mensagem)
