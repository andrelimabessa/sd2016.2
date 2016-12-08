from django.db import models
from django.core.urlresolvers import reverse
from django.utils import timezone
from django.contrib.auth.forms import User


class Jogo(models.Model):
	jogador1 = models.ForeignKey(User, related_name="jogador1")
	jogador2 = models.ForeignKey(User, related_name='jogador2')
	finalizado = models.BooleanField(default=False)
	iniciado = models.DateTimeField(default=timezone.now)
	jogadasMaxima = models.IntegerField(default=0)
	jogadasJogador1 = models.IntegerField(default=0)
	jogadasJogador2 = models.IntegerField(default=0)
	vencedor = models.ForeignKey(User, related_name="vencedor", null=True)

	def __str__(self):
		return "Jogo jogador1: " + self.jogador1.username + " vs jogador2:" + self.jogador2.username + ". Qtd Jogadas: " + str(self.jogadasMaxima) + ". Qtde Jog 1: " + str(self.jogadasJogador1) + ". Qtde Jog 2: " + str(self.jogadasJogador2) + ", vencedor: " + str(self.vencedor)

class Tabuleiro(models.Model):
    jogo = models.ForeignKey(Jogo, related_name="jogo")
    tamanho = models.IntegerField(default=0)

    def __str__(self):
        return "Tabuleiro do Jogo " + str(self.jogo)

class Posicao(models.Model):
    linha = models.IntegerField(default=0)
    coluna = models.IntegerField(default=0)
    barco = models.BooleanField(default=False)
    verificado = models.BooleanField(default=False)
    acerto = models.BooleanField(default=False)    
    tabuleiro = models.ForeignKey(Tabuleiro, related_name='tabuleiro', default=0)

    def __str__(self):
        return "Posicao [" + str(self.linha) + "][" + str(self.coluna) + "] barco=" + str(self.barco)