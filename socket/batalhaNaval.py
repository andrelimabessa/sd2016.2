from random import randint

#Arquivo Batalha Naval
#Contem lógica do jogo

class tabuleiro(object):

    print " "
    print "BATALHA NAVAL - O JOGO"
    print " "

    def __init__(auto, tabuleiro, numero, tamanho):
        auto.tabuleiro = tabuleiro
        auto.numero = numero
        auto.tamanho = tamanho

    def construir_tabuleiros(auto):
        for item in range(auto.tamanho):
            auto.tabuleiro.append(["O"] * auto.tamanho)

    def mostrar_tabuleiros(auto):
        print "Tabuleiro: %d" % auto.numero
        print " "
        for row in auto.tabuleiro:
            print ' '.join(row)
        print " "

    def criar_navios(auto):
        ship_col = randint(1, len(auto.tabuleiro))
        ship_row = randint(1, len(auto.tabuleiro[0]))
        return ship_col, ship_row

    def reiniciar(auto):
        del auto.tabuleiro[:]


class jogador(object):
    def __init__(auto, nome, vitorias, derrotas):
        auto.nome = nome
        auto.vitorias = vitorias
        auto.derrotas = derrotas

    def rodada_jogador(auto):
        pass
