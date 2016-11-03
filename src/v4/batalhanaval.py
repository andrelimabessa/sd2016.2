import os.path
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

	def salvarJogo(self):
		arq = open("log.txt", "w")
		
		## linha 0 | tamanho
		arq.write("{0}|".format(self.tamanho))		

		arq.write("\n")

		## linha 1 | jogadores		
		for jog in self.jogadores: 
			arq.write("{0}|".format(jog.nick))		

		arq.write("\n")
		
		## linha 2 | posições verificadas
		verificadas = self.tabuleiro.obterPosicoesVerificadas()
		for pos in verificadas:
			arq.write("{0},{1}|".format(pos["linha"], pos["coluna"]))
					
		arq.write("\n")
					
		## linha 3 | barcos
		barcos = self.tabuleiro.obterBarcos()		
		for pos in barcos:
			arq.write("{0},{1}|".format(pos["linha"], pos["coluna"]))
		
		arq.write("\n")
		
		## linha 4 | acertos
		acertos = self.tabuleiro.obterPosicoesAcerto()		
		for pos in acertos:
			arq.write("{0},{1}|".format(pos["linha"], pos["coluna"]))		

		print("\n*** jogo salvo ***")

	def carregarJogo(self):		
		arq = []
		
		if not os.path.exists("log.txt"):
			print("\n**** Nao ha dados de jogo salvo ****")
			return False
		else:
			arq = open("log.txt", "r")
			
			## linha 0
			linha0 = arq.readline()
			valores0 = linha0.split("|")			
			self.tamanho = int(valores0[0])			

			## linha 1
			linha1 = arq.readline()
			valores1 = linha1.split("|")
			for val1 in valores1:
				self.incluirJogador(val1)

			## linha 2 -- posições verificadas
			linha2 = arq.readline()		
			valores2 = linha2.split("|")
			for val2 in valores2:
				pos = val2.split(",")			
				if pos[0] != "\n" and pos[0] != "":
					self.tabuleiro.marcarPosicaoVerificada(int(pos[0]), int(pos[1]))			
					
			## linha 3 -- barcos
			linha3 = arq.readline()		
			valores3 = linha3.split("|")		
			for val3 in valores3:
				pos = val3.split(",")			
				if pos[0] != "\n" and pos[0] != "":
					self.tabuleiro.definirBarco(int(pos[0]), int(pos[1]))


			## linha 4 -- acertos
			linha4 = arq.readline()		
			valores4 = linha4.split("|")		
			for val4 in valores4:
				pos = val4.split(",")			
				if pos[0] != "\n" and pos[0] != "":
					self.tabuleiro.definirAcerto(int(pos[0]), int(pos[1]))				

			print("\n*** jogo carregado ***")				
			
			return True		