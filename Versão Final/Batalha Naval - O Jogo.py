import batalhaNaval
import sys

tamanho_tabuleiro_um = []
tamanho_tabuleiro_dois = []
total_rodadas = 0
mudar_estado_ganhador = 0

tabuleiro_um = batalhaNaval.tabuleiro(tamanho_tabuleiro_um, 1, 4)
tabuleiro_dois = batalhaNaval.tabuleiro(tamanho_tabuleiro_dois, 2, 4)
todos_tabuleiros = tabuleiro_um, tabuleiro_dois

primeiro_jogador = batalhaNaval.jogador('Jogador 1', 0, 0)
segundo_jogador = batalhaNaval.jogador('Jogador 2', 0, 0)

def carregar_jogo():

    map(lambda x: x.reiniciar(), todos_tabuleiros)
    tabuleiro_um.construir_tabuleiros()
    tabuleiro_dois.construir_tabuleiros()
    map(lambda x: x.mostrar_tabuleiros(), todos_tabuleiros)
    tabuleiro1_coluna, tabuleiro1_linha = tabuleiro_um.criar_navios()
    tabuleiro2_coluna, tabuleiro2_linha = tabuleiro_dois.criar_navios()
    return {
        'tabuleiro_um': (tabuleiro1_coluna, tabuleiro1_linha),
        'tabuleiro_dois': (tabuleiro2_coluna, tabuleiro2_linha)
    }

pontos_navio = carregar_jogo()

def rodada_jogador():
    if total_rodadas % 2 == 1:
        return primeiro_jogador
    else:
        return segundo_jogador

def jogar_novamente():

    global total_rodadas
    global pontos_navio
    resposta = str(raw_input("Voce gostaria de jogar novamente (s/n) ?"))
    if resposta == "s" or "S" or "sim" or "Sim" or "SIM":
        total_rodadas = 0
        pontos_navio = carregar_jogo()
    else:
        sys.sair()


def melhor_de(estado_ganhador, jogador):

    global total_rodadas
    if estado_ganhador == 1 and jogador.vitorias < 2:
        print "%s venceu o jogo!" % jogador.nome
    elif total_rodadas == 6:
        if estado_ganhador != 0:
            print "Este jogo empatou!"
    elif jogador.vitorias >= 2:
        print "%s ganhou a melhor de 3" % jogador.nome
    elif jogador.derrotas >= 2:
        print "%s perdeu a melhor de 3" % jogador.nome

    jogar_novamente()


def entrada_usuario(linha_navio, coluna_navio, jogador, tabuleiro, tamanho_tabuleiro):

    global mudar_estado_ganhador
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
        mudar_estado_ganhador = 1
        jogador.vitorias += 1
        print "Parabens! Voce afundou meu navio"
        melhor_de(mudar_estado_ganhador, jogador)
    elif ausente_tabuleiro:
        print "Oxi, voce acertou fora do mar."
    elif tabuleiro[escolha_linha][escolha_coluna] == "X":
        print "Voce ja usou essa combinacao."
    else:
        print "Nenhum navio foi atingido"
        tabuleiro[escolha_linha][escolha_coluna] = "X"
        mudar_estado_ganhador = 0

    map(lambda x: x.mostrar_tabuleiros(), todos_tabuleiros)
    return mudar_estado_ganhador

#Logica do Jogo

for jogos in range(3):
    jogos += 1
    for rodadas in range(6):
        total_rodadas += 1

        if rodada_jogador() == primeiro_jogador:
            print "Vez do %s" % primeiro_jogador.nome
            entrada_usuario(
                pontos_navio['tabuleiro_um'][0],
                pontos_navio['tabuleiro_um'][1],
                primeiro_jogador, tabuleiro_um.tabuleiro, tabuleiro_um.tamanho
            )
        elif rodada_jogador() == segundo_jogador:
            print "Vez do %s" % segundo_jogador.nome
            entrada_usuario(
                pontos_navio['tabuleiro_dois'][0],
                pontos_navio['tabuleiro_dois'][1],
                segundo_jogador, tabuleiro_dois.tabuleiro, tabuleiro_dois.tamanho
            )
        else:
            break
        if total_rodadas == 6 and rodada_jogador() == primeiro_jogador:
            melhor_de(mudar_estado_ganhador, primeiro_jogador)
        elif total_rodadas == 6 and rodada_jogador() == segundo_jogador:
            melhor_de(mudar_estado_ganhador, segundo_jogador)
        else:
            continue
    if jogos == 3:
            print "Fim do jogo."
            sair()
    else:
        continue