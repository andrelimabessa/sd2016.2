import random

class BatalhaNaval(object):

    def __init__(self):
        print("**************************************")
        print("Tabuleiro com Tamanho 5x5:")

        val = 5
        tam = int(val)
        self.tabuleiro = [[0 for i in range(tam)] for j in range(tam)]

        print("---------------------------------------------")
        print("Tabuleiro Criado!!!")
        print("Agora é  com você!!!")

    def imprimeTabuleiro(self):
        for i in self.tabuleiro:
            print (i)

    def insereNavios(self):
        i = 0
        pos = 0
        print("***********************************")

        while (i < 5):
            self.tabuleiro[pos][pos] = 1
            pos = random.randint(0,4)
            i+=1
        print("***Inserido Navios****") 


    def jogada(self, linha, coluna):

        quantJogada = 0
        jogue = 1
        jogadaErrada = 0
        jogadaCerta = 0
     

        print ("Coordenadas ( " + linha + ", " + coluna + " )")

        if (self.tabuleiro[int(linha)][int(coluna)] == 1):
            jogadaCerta+=1
            return "**** Acertou o Navio! ****"
        else:
            jogadaErrada+=1
            return "**** Errou Playboy! *****"


            jogue+=1
            quantJogada+=1
        
