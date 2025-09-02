def computador_escolhe_jogada(n, m):
    # Estratégia vencedora: deixar múltiplo de (m+1)
    retirada = n % (m + 1)
    if retirada == 0:
        retirada = min(m, n)
    return retirada


def usuario_escolhe_jogada(n, m):
    retirada = 0
    while retirada < 1 or retirada > m or retirada > n:
        retirada = int(input("Quantas peças você vai tirar? "))
        if retirada < 1 or retirada > m or retirada > n:
            print("Oops! Jogada inválida! Tente de novo.")
    return retirada


def partida():
    n = int(input("Quantas peças? "))
    m = int(input("Limite de peças por jogada? "))

    # Definir quem começa
    if n % (m + 1) == 0:
        print("\nVoce começa!\n")
        vez_do_computador = False
    else:
        print("\nComputador começa!\n")
        vez_do_computador = True

    while n > 0:
        if vez_do_computador:
            jogada = computador_escolhe_jogada(n, m)
            n -= jogada
            if jogada == 1:
                print("O computador tirou uma peça.")
            else:
                print(f"O computador tirou {jogada} peças.")

        else:
            jogada = usuario_escolhe_jogada(n, m)
            n -= jogada
            if jogada == 1:
                print("Voce tirou uma peça.")
            else:
                print(f"Voce tirou {jogada} peças.")

        # Mostrar peças restantes
        if n == 0:
            print("Fim do jogo! O computador ganhou!" if vez_do_computador else "Fim do jogo! Você ganhou!")
        elif n == 1:
            print("Agora resta apenas uma peça no tabuleiro.\n")
        else:
            print(f"Agora restam {n} peças no tabuleiro.\n")

        vez_do_computador = not vez_do_computador


def campeonato():
    placar_usuario = 0
    placar_computador = 0

    print("\nVoce escolheu um campeonato!\n")

    for rodada in range(1, 4):
        print(f"**** Rodada {rodada} ****\n")
        vencedor = partida()
        if vencedor == "usuario":
            placar_usuario += 1
        else:
            placar_computador += 1

    print("**** Final do campeonato! ****\n")
    print(f"Placar: Você {placar_usuario} X {placar_computador} Computador")


def main():
    print("Bem-vindo ao jogo do NIM! Escolha:\n")
    print("1 - para jogar uma partida isolada")
    print("2 - para jogar um campeonato")

    escolha = int(input())

    if escolha == 1:
        print("\nVoce escolheu uma partida isolada!\n")
        partida()
    elif escolha == 2:
        campeonato()


if __name__ == "__main__":
    main()