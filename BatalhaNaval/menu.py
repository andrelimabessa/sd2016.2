class Menu(object):

    def exibeMenu(self):

        print("*********************************************\n")
        print("           Vamos Jogar Batalha Naval!       \n")
        print("*********************************************\n")
        print("Escolha uma das Opcoes?\n")
        print("1 - * Jogar *")
        print("2 - * Informar Jogada *")

        opcao = input('\n')

        mpOpcao = {}
        mpOpcao["opcao"] = opcao

        if opcao == "2":
            posX = input("Informe a Coordenada X:\n")
            posY = input("Informe a Coordenada Y:\n")
            mpOpcao["posX"] = posX
            mpOpcao["posY"] = posY

        return str(mpOpcao)
