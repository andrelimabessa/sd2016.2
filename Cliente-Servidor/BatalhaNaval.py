import random


class BatalhaNaval(object):

	def __init__(self):
		self.tabuleiro = [ [ "A" for j in range(5) ] for i in range(5)]
		self.numMaximoJogadas = 3
		self.preencherTabuleiro()


	def preencherTabuleiro(self):
		for i in range(2):
			x = random.randint(0,4)
			y = random.randint(0,4)
			if self.tabuleiro[x][y] == "B":
				i -= 1
			else:
				print(str(x)+"-"+str(y))
				self.tabuleiro[x][y] = "B"


	def jogada(self, jogadaEixoX, jogadaEixoY):
		if self.tabuleiro[jogadaEixoX][jogadaEixoY] == "B":
			self.tabuleiro[jogadaEixoX][jogadaEixoY] = "X"
			msn = "Barco Afundado!"
			self.numMaximoJogadas -= 1

		elif self.tabuleiro[jogadaEixoX][jogadaEixoY] == "A":
			msn= "Tiro na água!"
			self.numMaximoJogadas -= 1
		else:
			msn = "Barco já afundado!"

		return msn

