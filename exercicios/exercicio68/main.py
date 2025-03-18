from cadastro import cadastrar_aluno, listar_alunos, mostrar_dados_aluno, atualizar_aluno, remover_aluno # type: ignore

def exibir_menu():
    print("\nMenu de operações:")
    print("1 - Cadastrar aluno")
    print("2 - Atualizar dados do aluno")
    print("3 - Remover aluno")
    print("4 - Listar todos os alunos")
    print("5 - Mostrar dados de um aluno específico")
    print("6 - Sair")

def executar_programa():
    while True:
        exibir_menu()
        opcao = input('Escolha uma opção (1-6): ')
        
        if opcao == '1':
            cadastrar_aluno()
        elif opcao == '2':
            atualizar_aluno()
        elif opcao == '3':
            remover_aluno()
        elif opcao == '4':
            listar_alunos()
        elif opcao == '5':
            mostrar_dados_aluno()
        elif opcao == '6':
            print('Sistema encerrado. Até logo!')
            break
        else:
            print('Opção inválida. Tente novamente.')

executar_programa()
