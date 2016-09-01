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
			if self.tabuleiro.verificarJogada(i, j):
				self.jogadaRestante -= 1
		else:
			print("////// Sem jogadas restante ///////")

	def salvarJogo(self):
		arq = open("log.txt", "w")
		
		## linha 1 | status
		arq.write("{0}|{1}".format(self.tamanho, self.jogadaRestante))

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
			
	def obterJogadasRealizadas(self):
		lista = self.tabuleiro.obterPosicoesVerificadas()
		retorno = [{item["linha"], item["coluna"]} for item in lista]
		return retorno
		
	def obterAcertos(self):
		lista = self.tabuleiro.obterPosicoesAcerto()
		retorno = [{item["linha"], item["coluna"]} for item in lista]
		return retorno
	
	def carregarJogo(self):
		arq = open("log.txt", "r")
		
		## linha 1
		linha1 = arq.readline()
		valores = linha1.split("|")
		self.tamanho = int(valores[0])
		self.jogadaRestante = int(valores[1])		
		
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
		