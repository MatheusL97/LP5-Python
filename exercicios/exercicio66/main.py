
from operacoes.cadastro import cadastrar_nome, atualizar_nome, excluir_nome, listar_nomes # type: ignore

def exibir_menu():
    print("\nMenu de operações:")
    print("1 - Cadastrar nome")
    print("2 - Atualizar nome")
    print("3 - Excluir nome")
    print("4 - Listar todos os cadastrados")
    print("5 - Sair")

def executar_programa():
    while True:
        exibir_menu()
        opcao = input('Escolha uma opção (1-5): ')
        
        if opcao == '1':
            cadastrar_nome()
        elif opcao == '2':
            atualizar_nome()
        elif opcao == '3':
            excluir_nome()
        elif opcao == '4':
            listar_nomes()
        elif opcao == '5':
            print('Programa encerrado. Até logo!')
            break
        else:
            print('Opção inválida. Tente novamente.')
        
        continuar = input('Deseja realizar outra operação? (s/n): ')
        if continuar.lower() != 's':
            print('Programa encerrado. Até logo!')
            break

executar_programa()
