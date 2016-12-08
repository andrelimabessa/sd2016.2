from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from jogo.models import Jogo, Tabuleiro, Posicao
from jogada.models import Jogada

TAMANHO = 5

class BatalhaNaval(object):
    def __init__(self):
        self.tabuleiro = {}

    def tabuleiroGerar(self, jogo):
        tab = Tabuleiro(jogo=jogo, tamanho=TAMANHO)
        tab.save()

        barco = False

        for posI in range(tab.tamanho):
            for posJ in range(tab.tamanho):
                if (posI == 1 and posJ == 1) or (posI == 2 and posJ == 2) or (posI == 3 and posJ == 3) or (posI == 4 and posJ == 4):
                    barco = True
                else:
                    barco = False

                Posicao(linha=posI, coluna=posJ, barco=barco, tabuleiro=tab).save()

        return tab

    def tabuleiroAtualizar(self, jogada):
        tabuleiro = Tabuleiro.objects.get(jogo=jogada.jogo)

        # define posição como verificada e se é um acerto
        posicao = Posicao.objects.get(tabuleiro=tabuleiro, linha=jogada.linha, coluna=jogada.coluna)
        posicao.verificado = True
        if posicao.barco == True:
            posicao.acerto = True
        else:
            posicao.acerto = False

        jogada.acerto = posicao.acerto
        posicao.save()
        jogada.save()

    def permiteJogada(self, jogada):
        if int(jogada.linha) >= TAMANHO or int(jogada.coluna) >= TAMANHO:
            return "Posição excede tamanho do tabuleiro ", TAMANHO-1

        if not self.verificarQtdeJogadas(jogada):
            return "Jogador já utilizou todas as suas jogadas ", str(jogada.jogo.jogador1), str(jogada.jogo.jogador2)
        
        if self.verificarJogadaRealizada(jogada):
            return "Esta jogada já foi realizada"
        
        return ""
    
    def verificarQtdeJogadas(self, jogada):
        qtde = 0
        # verifica quem é o autor da jogada
        if jogada.autor.pk == jogada.jogo.jogador1.pk:
            qtde = jogada.jogo.jogadasJogador1 
        else:             
            qtde = jogada.jogo.jogadasJogador2

        if qtde < jogada.jogo.jogadasMaxima:
            return True
        else:
            return False

    def verificarJogadaRealizada(self, jogada):
        jogadaArmazenada = Jogada.objects.filter(jogo=jogada.jogo).filter(linha=jogada.linha).filter(coluna=jogada.coluna)
        
        return jogadaArmazenada

    def jogoAtualizar(self, jogada):
        jogador = jogada.autor
        jogo = jogada.jogo        

        if jogo.jogador1 == jogador:
            jogo.jogadasJogador1 += 1
        else:
            jogo.jogadasJogador2 += 1
                
        jogo.save()            

    def atualizarVencedor(self, jogada):
        jogoAtual = Jogo.objects.get(pk=jogada.jogo.id)
        
        acertosJogador1 = 0
        acertosJogador2 = 0 
        # se não há mais jogadas disponíveis
        if jogoAtual.jogadasJogador1 == jogoAtual.jogadasMaxima and jogoAtual.jogadasJogador2 == jogoAtual.jogadasMaxima:
            acertosJogador1 = len(Jogada.objects.filter(jogo_id=jogoAtual.id).filter(autor_id=jogoAtual.jogador1.id).filter(acerto=True))
            acertosJogador2 = len(Jogada.objects.filter(jogo_id=jogoAtual.id).filter(autor_id=jogoAtual.jogador2.id).filter(acerto=True))

            jogoAtual.finalizado = True
            if acertosJogador1 == acertosJogador2:
                jogoAtual.vencedor = None
            elif acertosJogador1 > acertosJogador2:
                jogoAtual.vencedor = jogoAtual.jogador1
            else:
                jogoAtual.vencedor = jogoAtual.jogador2
            
            jogoAtual.save()

    def atualizar(self, jogada):        
        self.tabuleiroAtualizar(jogada)
        self.jogoAtualizar(jogada)
        self.atualizarVencedor(jogada)