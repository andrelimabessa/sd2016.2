import posicao
import tabuleiro

class BatalhaNaval(object):	

	def __init__(self, tamanho, qtdeJogadas):
		self.tamanho = tamanho
		self.tabuleiro = tabuleiro.Tabuleiro(tamanho)
		self.jogadaRestante = qtdeJogadas
		self.ativa = "N"		
		
	def definirTabuleiro(self):
		self.ativa = "S"
		self.tabuleiro.inicializar()
		
	def atirar(self, i, j):
		if self.jogadaRestante > 0:
			self.tabuleiro.verificarJogada(i, j)
			self.jogadaRestante -= 1
		else:
			print("////// Sem jogadas restante ///////")

	def salvarJogo(self):
		arq = open("log.txt", "w")
		
		arq.write("{0}|{1}".format(self.tamanho, self.jogadaRestante))
		print("--- jogo salvo ---")
		
##		verificadas = self.tabuleiro.obterPosicoesNaoVerificadas()		
##		print("##verificadas")
##		for pos in verificadas:			
##			arq.write("")
##			arq.write("{0},{1}".format(pos["linha"], pos["coluna"]))

	def carregarJogo(self):
		arq = open("log.txt", "r")
		linha = arq.readline()
		valores = linha.split("|")
		self.tamanho = int(valores[0])
		self.jogadaRestante = int(valores[1])
		print("--- jogo carregado ---")		
		