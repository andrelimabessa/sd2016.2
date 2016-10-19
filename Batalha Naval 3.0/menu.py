import batalhaNaval
import sys

batalha = batalhaNaval.batalha();

#Logica do Jogo
for jogos in range(3):
    jogos += 1
    for rodadas in range(6):
        batalha.total_rodadas += 1

        if batalha.rodada_jogador() == batalha.primeiro_jogador:
            print "Vez do %s" % batalha.primeiro_jogador.nome
            batalha.entrada_usuario(
                batalha.pontos_navio['tabuleiro_um'][0],
                batalha.pontos_navio['tabuleiro_um'][1],
                batalha.primeiro_jogador, batalha.tabuleiro_um.tabuleiro, batalha.tabuleiro_um.tamanho
            )
        elif batalha.rodada_jogador() == batalha.segundo_jogador:
            print "Vez do %s" % batalha.segundo_jogador.nome
            batalha.entrada_usuario(
                batalha.pontos_navio['tabuleiro_dois'][0],
                batalha.pontos_navio['tabuleiro_dois'][1],
                batalha.segundo_jogador, batalha.tabuleiro_dois.tabuleiro, batalha.tabuleiro_dois.tamanho
            )
        else:
            break
        if batalha.total_rodadas == 6 and batalha.rodada_jogador() == batalha.primeiro_jogador:
            batalha.melhor_de(batalha.mudar_estado_ganhador, batalha.primeiro_jogador)
        elif batalha.total_rodadas == 6 and batalha.rodada_jogador() == batalha.segundo_jogador:
            batalha.melhor_de(batalha.mudar_estado_ganhador, batalha.segundo_jogador)
        else:
            continue
    if jogos == 3:
            print "Fim do jogo."
            sair()
    else:
        continue

raw_input("Clique para sair")