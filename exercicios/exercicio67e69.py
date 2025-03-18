def exibir_tabuleiro(tabuleiro):
    print(f"{tabuleiro[0]} | {tabuleiro[1]} | {tabuleiro[2]}")
    print("--+---+--")
    print(f"{tabuleiro[3]} | {tabuleiro[4]} | {tabuleiro[5]}")
    print("--+---+--")
    print(f"{tabuleiro[6]} | {tabuleiro[7]} | {tabuleiro[8]}")

def verificar_vencedor(tabuleiro, jogador):
    vitoria_combinacoes = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Linhas
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Colunas
        [0, 4, 8], [2, 4, 6]  # Diagonais
    ]
    for combinacao in vitoria_combinacoes:
        if tabuleiro[combinacao[0]] == tabuleiro[combinacao[1]] == tabuleiro[combinacao[2]] == jogador:
            return True
    return False

def jogar():
    tabuleiro = [" "]*9  
    jogador_atual = "X" 
    vencedor = False
    jogadas = 0

    while not vencedor and jogadas < 9:
        exibir_tabuleiro(tabuleiro)
        print(f"Vez do jogador {jogador_atual}")


        jogada = -1
        while jogada not in range(9) or tabuleiro[jogada] != " ":
            try:
                jogada = int(input(f"Escolha uma posição (0-8): "))
            except ValueError:
                print("Entrada inválida. Tente novamente.")
                continue


        tabuleiro[jogada] = jogador_atual
        jogadas += 1


        if verificar_vencedor(tabuleiro, jogador_atual):
            vencedor = True
            exibir_tabuleiro(tabuleiro)
            print(f"Jogador {jogador_atual} venceu!")
        else:
            jogador_atual = "O" if jogador_atual == "X" else "X"

    if not vencedor:
        exibir_tabuleiro(tabuleiro)
        print("Empate!")

jogar()
