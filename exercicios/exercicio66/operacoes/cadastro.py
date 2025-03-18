cadastros = []

def cadastrar_nome():
    nome = input('Digite o nome para cadastrar: ')
    cadastros.append(nome)
    print(f'Nome "{nome}" cadastrado com sucesso!')


def atualizar_nome():
    nome_antigo = input('Digite o nome que deseja atualizar: ')
    if nome_antigo in cadastros:
        novo_nome = input('Digite o novo nome: ')
        index = cadastros.index(nome_antigo)
        cadastros[index] = novo_nome
        print(f'Nome "{nome_antigo}" atualizado para "{novo_nome}".')
    else:
        print(f'O nome "{nome_antigo}" não foi encontrado.')


def excluir_nome():
    nome = input('Digite o nome que deseja excluir: ')
    if nome in cadastros:
        cadastros.remove(nome)
        print(f'Nome "{nome}" excluído com sucesso!')
    else:
        print(f'O nome "{nome}" não foi encontrado.')


def listar_nomes():
    if cadastros:
        print("Nomes cadastrados:")
        for nome in cadastros:
            print(nome)
    else:
        print('Nenhum nome cadastrado.')
