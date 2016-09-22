class Batle_Field(object):

    def __init__(self,tam):
        self.tabuleiro = [[0 for i in range(int(tam))] for j in range(int(tam))]
        for i in range(int(tam)):
            for j in range(int(tam)):
                self.tabuleiro[i][j] = "A"
        
    def criandotab(self,tam,navios):
        import sys
        import random

        for i in range(int(navios)):
            xps1 = random.randint(0,int(tam)-1)
            yps2 = random.randint(0,int(tam)-1)
            self.tabuleiro[xps1][yps2] = "N"

        print(self.tabuleiro)

        arq = open("arqdados.txt", "a")
        arq.write(str(self.tabuleiro))
        arq.close()

    def jogar(self,posicaoX,posicaoY):
        import sys
        try:
            arq = open("arqdados.txt", "r")


            for linha in arq:
                print(linha)

            arq.close()

            if self.tabuleiro[int(posicaoX)][int(posicaoY)]=="N":
                self.tabuleiro[int(posicaoX)][int(posicaoY)]="ok"

                arq = open("arqdados.txt", "w")
                arq.write(str(self.tabuleiro))
                arq.close()

                return True
            else:
                return False
        except:
            val = sys.exc_info()[0]
            print(val)
