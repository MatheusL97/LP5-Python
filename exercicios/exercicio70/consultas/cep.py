import requests # type: ignore

def consultar_cep(cep):
    url = f"https://viacep.com.br/ws/{cep}/json/"
    resposta = requests.get(url)
    return resposta.json()

def exibir_relatorio(endereco):
    print("\n--- Relatório de Endereço ---")
    print(f"CEP: {endereco['cep']}")
    print(f"Rua: {endereco['logradouro']}")
    print(f"Bairro: {endereco['bairro']}")
    print(f"Cidade: {endereco['localidade']}")
    print(f"Estado: {endereco['uf']}")
    print("----------------------------\n")
