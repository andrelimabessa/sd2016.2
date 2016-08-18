class BatalhaNaval(object):

	AGUA = 0
	NAVIO = 1
	NAUFRAGIO = 'X'

	def __init__(self, w, h):
		self.tabuleiro = [[self.AGUA for x in range(w)] for y in range(h)] 

	def insereNavio(self, x, y):
		self.tabuleiro[x][y] = self.NAVIO

	def destroiNavio(self, x, y):
		if self.tabuleiro[x][y] == self.NAVIO:
			self.tabuleiro[x][y] = self.NAUFRAGIO

	def exibeTabuleiro(self):
		for i in range(len(self.tabuleiro)):
			linha = "|"
			for j in range(len(self.tabuleiro[i])):
				if self.tabuleiro[i][j] == self.AGUA:
					linha = linha + " " + "AGUA" + " |"
				elif self.tabuleiro[i][j] == self.NAVIO:
					linha = linha + " " + "NAVIO" + " |"
				elif self.tabuleiro[i][j] == self.NAUFRAGIO:
					linha = linha + " " + "NAUFRAGIO" + " |"
			print(linha)

	def exibeTabuleiroSimples(self):
		for i in range(len(self.tabuleiro)):
			print(self.tabuleiro[i])