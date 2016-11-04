import random

class batalhaNaval(object):
    def __init__(self,qtdJogadas):
        self.tabuleiro = [["A" for j in range(5)] for i in range(5)]
        self.qtdJogadas = qtdJogadas
        self.qtdBarcos = 2
        if self.existeJogoSalvo():
            self.carregarTabuleiro()
            self.carregarJogadas()
        else:
            self.preencherTabuleiro()

    def preencherTabuleiro(self):
        for i in range(2):
            x = random.randint(0,4)
            y = random.randint(0,4)
            if self.tabuleiro[x][y] == "B":
                i=-1
            else:
                print(str(x) + "-" + str(y))
                self.tabuleiro[x][y] = "B"
                self.salvarTabuleiro(x,y,"B")

    def existeJogoSalvo(self):
        arq = open("DadosdoTabuleiro.txt", "r")
        if arq.readline() == "":
            existe = False
        else:
            existe = True
        return existe

    def salvarJogadas(self):
        self.arq = open("DadosdeJogadas.txt", "w")
        self.arq.write(str(self.qtdJogadas))
        self.arq.close()

    def salvarTabuleiro(self, eixoX, eixoY, valor):
        self.arq = open("DadosdoTabuleiro.txt", "w")
        self.arq.write(str(eixoX) + "-" + str(eixoY) + "-" + str(valor) + "\n")
        self.arq.close()

    def carregarJogadas(self):
        arq = open("DadosdeJogadas.txt", "r")
        for linha in arq:
            self.qtdJogadas = int(linha)
        arq.close()

    def carregarTabuleiro(self):
        arq = open("DadosdoTabuleiro.txt", "r")
        for linha in arq:
            valor = linha.split("-")
            self.tabuleiro[int(valor[0])][int(valor[1])] = "B"
        arq.close()


    def jogada(self):

        jogadaEixoX = int(input("Digite a posicao do eixo X:"))
        jogadaEixoY = int(input("Digite a posicao do eixo Y:"))

        if self.tabuleiro[jogadaEixoX][jogadaEixoY] == "B":
            self.tabuleiro[jogadaEixoX][jogadaEixoY] = "X"
            self.salvarTabuleiro(jogadaEixoX, jogadaEixoY, "X")
            print("Navio Afundado!")
            self.qtdJogadas -= 1
            self.qtdBarcos -= 1
            self.salvarJogadas()

        elif self.tabuleiro[jogadaEixoX][jogadaEixoY] == "A":
            print("Tiro atingiu a água!")
            self.qtdJogadas -= 1
            self.salvarJogadas()
        else:
            print("Navio já afundado!")


    def limparLogs(self):
        self.arq = open("DadosdeJogadas.txt", "w")
        self.arq.close()
        self.arq = open("DadosdoTabuleiro.txt", "w")
        self.arq.close()
