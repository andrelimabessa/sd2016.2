import random


class BatalhaNaval(object):

	def __init__(self):
		self.tabuleiro = [ [ "~" for j in range(5) ] for i in range(5)]
		self.numMaximoJogadas = 3
		self.preencherTabuleiro()
		self.acertos = 0


	def preencherTabuleiro(self):
		for i in range(2):
			x = random.randint(0,4)
			y = random.randint(0,4)
			if self.tabuleiro[x][y] == "@":
				i -= 1
			else:
				print(str(x)+"-"+str(y))
				self.tabuleiro[x][y] = "@"


	def jogada(self, jogadaEixoX, jogadaEixoY):
		if self.tabuleiro[jogadaEixoX][jogadaEixoY] == "@":
			self.tabuleiro[jogadaEixoX][jogadaEixoY] = "*"
			msn = "Acertou o barco!"
			self.numMaximoJogadas -= 1
			self.acertos += 1

		elif self.tabuleiro[jogadaEixoX][jogadaEixoY] == "~":
			msn= "Acertou a agua!"
			self.numMaximoJogadas -= 1

		return msn

