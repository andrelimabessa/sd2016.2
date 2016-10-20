from jogador import Jogador
from tabuleiro import Tabuleiro

class BatalhaNaval(object):

	def __init__(self, tamanho, qtdeJogadas):
		self.tamanho = tamanho
		self.tabuleiro = Tabuleiro(tamanho)
		self.ativa = "N"
		self.jogadores = []	
		self.definirTabuleiro()

	# inicializa posições do tabuleiro
	# posições de barcos estão definidas no código
	def definirTabuleiro(self):
		self.ativa = "S"
		self.tabuleiro.inicializar()	

	# Inclui jogador na lista mantida na memória
	def incluirJogador(self, nick):
		existe = self.verificarExistenciaJogador(nick)
		if existe == True:
			raise Exception("Nick de jogador já utilizado: " + nick)

		
		# cria instância de jogador,
		# informado o nick e a quantidade de jogadas inicial
		jogador = Jogador(nick, 5)
		self.jogadores.append(jogador)

		return jogador

	def getQuantidadeJogador(self):
		return len(self.jogadores)

	def obterJogadasRealizadas(self):
		lista = self.tabuleiro.obterPosicoesVerificadas()
		retorno = [{item["linha"], item["coluna"]} for item in lista]
		return retorno

	# verifica se para o jogador informado
	# existe jogada restante
	def possuiJogadaRestante(self, nick):
		jogador = [x for x in self.jogadores if x.nick == nick][0]
		return jogador.jogadaRestante > 0

	# verifica se o nick está registrado
	# para outro jogador
	def verificarExistenciaJogador(self, nick):
		jogador = [x for x in self.jogadores if x.nick == nick]
		return len(jogador) > 0	


	def atirar(self, nick, i, j):
		jogador = [x for x in self.jogadores if x.nick == nick][0]

		if jogador.jogadaRestante > 0:

			if self.tabuleiro.posicaoVerificada(i, j):
				return 0;

			resultado = self.tabuleiro.verificarJogada(i, j)			
			jogador.jogadaRestante -= 1			

			if resultado == True:
				return 1 # Barco
			else: 
				return 2 # Água
		else:
			print("////// Sem jogadas restante ///////")
