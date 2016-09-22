from batlefield import Batle_Field

class Hello(object):

    def jogo(self):

        print("----------------------------")
        print("Vamos começar a Batalha Naval")
        print("----------------------------\n")

        tam = input("Digite o tamanho da matriz  ------/")

        navios = input("Digite a quantidade de navios  -------/")

        b = Batle_Field(tam)

        b.criandotab(tam,navios)

        for i in range(int(tam)):
            posicaoX = input("Numero da posicao x  ----/")
            posicaoY = input("Numero da posicao y  ----/")

            if b.jogar(posicaoX, posicaoY):
                print("ACERTOU")
            else:
                print("ERROU")

input()