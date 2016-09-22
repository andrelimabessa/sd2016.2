class Menu(object):
    print("1 - Começar a Jogar")
    print("2 - Sair")

    opcao = input("Digite o numero da opcao desejada ------/" )

    if int(opcao)==1:
        from batalha import Hello

        h = Hello()

        h.jogo()
    else:
        exit()


