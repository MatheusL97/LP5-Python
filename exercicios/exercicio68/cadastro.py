import random

alunos = []

def gerar_matricula():
    return str(random.randint(100000, 999999))

def cadastrar_aluno():
    nome = input('Digite o nome do aluno: ')
    email = input('Digite o e-mail do aluno: ')
    data_nascimento = input('Digite a data de nascimento do aluno (DD/MM/AAAA): ')
    
    matricula = gerar_matricula()

    aluno = {
        'nome': nome,
        'email': email,
        'data_nascimento': data_nascimento,
        'matricula': matricula
    }

    alunos.append(aluno)
    print(f'Aluno cadastrado com sucesso! Matrícula: {matricula}')

def listar_alunos():
    if not alunos:
        print("Nenhum aluno cadastrado.")
        return
    
    for aluno in alunos:
        print(f"\nMatrícula: {aluno['matricula']}")
        print(f"Nome: {aluno['nome']}")
        print(f"E-mail: {aluno['email']}")
        print(f"Data de Nascimento: {aluno['data_nascimento']}")
        print("-" * 30)

def mostrar_dados_aluno():
    matricula = input('Digite a matrícula do aluno: ')
    
    for aluno in alunos:
        if aluno['matricula'] == matricula:
            print(f"\nMatrícula: {aluno['matricula']}")
            print(f"Nome: {aluno['nome']}")
            print(f"E-mail: {aluno['email']}")
            print(f"Data de Nascimento: {aluno['data_nascimento']}")
            print("-" * 30)
            return
    
    print("Aluno não encontrado com essa matrícula.")

def atualizar_aluno():
    matricula = input('Digite a matrícula do aluno para atualização: ')

    for aluno in alunos:
        if aluno['matricula'] == matricula:
            print(f"Aluno encontrado: {aluno['nome']}")
            campo = input("Qual dado deseja atualizar? (nome, email, data_nascimento): ").lower()
            
            if campo == "nome":
                aluno['nome'] = input("Digite o novo nome: ")
            elif campo == "email":
                aluno['email'] = input("Digite o novo e-mail: ")
            elif campo == "data_nascimento":
                aluno['data_nascimento'] = input("Digite a nova data de nascimento (DD/MM/AAAA): ")
            else:
                print("Opção inválida.")
            return

    print("Aluno não encontrado com essa matrícula.")

def remover_aluno():
    matricula = input('Digite a matrícula do aluno para remoção: ')

    for aluno in alunos:
        if aluno['matricula'] == matricula:
            alunos.remove(aluno)
            print(f"Aluno {aluno['nome']} removido com sucesso.")
            return
    
    print("Aluno não encontrado com essa matrícula.")
