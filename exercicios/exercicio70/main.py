from consultas.cep import consultar_cep, exibir_relatorio

def executar_programa():
    while True:
        cep = input("Digite o CEP (somente números): ").strip()

        if len(cep) != 8 or not cep.isdigit():
            print("CEP inválido! O CEP deve ter exatamente 8 dígitos numéricos.")
            continue
        
        endereco = consultar_cep(cep)

        if "erro" in endereco:
            print("CEP não encontrado. Por favor, tente novamente.")
            continue
        else:
            exibir_relatorio(endereco)
        
        nova_consulta = input("Deseja realizar outra consulta? (s/n): ").strip().lower()
        if nova_consulta != 's':
            print("Sistema encerrado. Até logo!")
            break

executar_programa()
