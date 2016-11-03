import random


class BatalhaNaval(object):

	def __init__(self):
		self.tabuleiro = [ [ "A" for j in range(5) ] for i in range(5)]
		self.numMaximoJogadas = 3
		if self.existeJogoSalvo():
			self.carregarTabuleiro()
			self.carregarQntJogadas()
		else:
			self.preencherTabuleiro()
		#self.preencherTabuleiro()


	def preencherTabuleiro(self):
		for i in range(2):
			x = random.randint(0,4)
			y = random.randint(0,4)
			if self.tabuleiro[x][y] == "B":
				i -= 1
			else:
				print(str(x)+"-"+str(y))
				self.tabuleiro[x][y] = "B"
				self.saveTabuleiro(x, y, "B")


	def jogada(self, jogadaEixoX, jogadaEixoY):
		if self.tabuleiro[jogadaEixoX][jogadaEixoY] == "B":
			self.tabuleiro[jogadaEixoX][jogadaEixoY] = "X"
			self.saveTabuleiro(jogadaEixoX, jogadaEixoY, "X")
			msn = "Barco Afundado!"
			self.numMaximoJogadas -= 1
			self.saveQntJogadas()

		elif self.tabuleiro[jogadaEixoX][jogadaEixoY] == "A":
			msn= "Tiro na água!"
			self.numMaximoJogadas -= 1
			self.saveQntJogadas()
		else:
			msn = "Barco já afundado!"

		return msn

	def existeJogoSalvo(self):
		arq = open("LogTabuleiro.txt", "r")
		if arq.readline() == "":
			existe = False
		else:
			existe = True
		return existe

	def saveQntJogadas(self):
		self.arq = open("LogJogadas.txt", "w")
		self.arq.write(str(self.numMaximoJogadas))
		self.arq.close()

	def saveTabuleiro(self, eixoX, eixoY, valor):
		self.arq = open("LogTabuleiro.txt", "a")
		self.arq.write(str(eixoX) + "-" + str(eixoY) + "-" + str(valor) + "\n")
		self.arq.close()

	def carregarTabuleiro(self):
		arq = open("LogTabuleiro.txt", "r")
		for linha in arq:
			valor = linha.split("-")
			self.tabuleiro[int(valor[0])][int(valor[1])] = valor[2]

		arq.close()

	def carregarQntJogadas(self):
		arq = open("LogJogadas.txt", "r")
		for linha in arq:
			self.numMaximoJogadas = int(linha)

		arq.close()

	def limparLogs(self):
		self.arq = open("LogJogadas.txt", "w")
		self.arq.close()
		self.arq = open("LogTabuleiro.txt", "w")
		self.arq.close()
