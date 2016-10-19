from random import randint

#Arquivo Batalha Naval
#Contem logica do jogo

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

class batalha(object):
    def __init__(auto):
        auto.tamanho_tabuleiro_um = []
        auto.tamanho_tabuleiro_dois = []
        auto.total_rodadas = 0
        auto.mudar_estado_ganhador = 0

        auto.tabuleiro_um = tabuleiro(auto.tamanho_tabuleiro_um, 1, 4)
        auto.tabuleiro_dois = tabuleiro(auto.tamanho_tabuleiro_dois, 2, 4)
        auto.todos_tabuleiros = auto.tabuleiro_um, auto.tabuleiro_dois

        auto.primeiro_jogador = jogador('Jogador 1', 0, 0)
        auto.segundo_jogador = jogador('Jogador 2', 0, 0)

        auto.pontos_navio = auto.carregar_jogo()

    def carregar_jogo(auto):
        map(lambda x: x.reiniciar(), auto.todos_tabuleiros)
        auto.tabuleiro_um.construir_tabuleiros()
        auto.tabuleiro_dois.construir_tabuleiros()
        map(lambda x: x.mostrar_tabuleiros(), auto.todos_tabuleiros)
        tabuleiro1_coluna, tabuleiro1_linha = auto.tabuleiro_um.criar_navios()
        tabuleiro2_coluna, tabuleiro2_linha = auto.tabuleiro_dois.criar_navios()
        return {
            'tabuleiro_um': (tabuleiro1_coluna, tabuleiro1_linha),
            'tabuleiro_dois': (tabuleiro2_coluna, tabuleiro2_linha)
        }

    def entrada_usuario(auto, linha_navio, coluna_navio, jogador, tabuleiro, tamanho_tabuleiro):
        auto.mudar_estado_ganhador
        escolha_coluna = 0
        escolha_linha = 0
        while True:
            try:
                escolha_linha = int(raw_input("Escolha a linha:")) - 1
                escolha_coluna = int(raw_input("Escolha a coluna:")) - 1
            except ValueError:
                print "Por favor, insira apenas numeros."
                continue
            else:
                break
        partida = escolha_linha == linha_navio - 1 and escolha_coluna == coluna_navio - 1
        ausente_tabuleiro = (escolha_linha < 0 or escolha_linha > tamanho_tabuleiro - 1) \
                       or (escolha_coluna < 0 or escolha_coluna > tamanho_tabuleiro - 1)
        if partida:
            auto.mudar_estado_ganhador = 1
            jogador.vitorias += 1
            print "Parabens! Voce afundou meu navio"
            melhor_de(auto.mudar_estado_ganhador, jogador)
        elif ausente_tabuleiro:
            print "Oxi, voce acertou fora do mar."
        elif tabuleiro[escolha_linha][escolha_coluna] == "X":
            print "Voce ja usou essa combinacao."
        else:
            print "Nenhum navio foi atingido"
            tabuleiro[escolha_linha][escolha_coluna] = "X"
            auto.mudar_estado_ganhador = 0

        map(lambda x: x.mostrar_tabuleiros(), auto.todos_tabuleiros)
        return auto.mudar_estado_ganhador

    def rodada_jogador(auto):
        if auto.total_rodadas % 2 == 1:
            return auto.primeiro_jogador
        else:
            return auto.segundo_jogador

    def jogar_novamente(auto):
        resposta = str(raw_input("Voce gostaria de jogar novamente (s/n) ?"))
        if resposta == "s" or "S" or "sim" or "Sim" or "SIM":
            auto.total_rodadas = 0
            auto.pontos_navio = auto.carregar_jogo()
        else:
            sys.sair()


    def melhor_de(auto, estado_ganhador, jogador):
        if estado_ganhador == 1 and jogador.vitorias < 2:
            print "%s venceu o jogo!" % jogador.nome
        elif auto.total_rodadas == 6:
            if estado_ganhador != 0:
                print "Este jogo empatou!"
        elif jogador.vitorias >= 2:
            print "%s ganhou a melhor de 3" % jogador.nome
        elif jogador.derrotas >= 2:
            print "%s perdeu a melhor de 3" % jogador.nome

        auto.jogar_novamente()